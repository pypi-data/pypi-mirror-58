"""
The ``train`` subcommand can be used to either train a model locally or in Polyaxon environment.
It requires a configuration file and a directory in which to write the results (path or $POLYAXON_RUN_OUTPUTS_PATH).

.. code-block:: bash

   $ allennlp train --help
    usage: allennlp train [-h] -s SERIALIZATION_DIR [-r] [-f] [-o OVERRIDES]
                          [--file-friendly-logging]
                          [--cache-directory CACHE_DIRECTORY]
                          [--cache-prefix CACHE_PREFIX]
                          [--include-package INCLUDE_PACKAGE]
                          param_path

    Train the specified model on the specified dataset.

    positional arguments:
      param_path            path to parameter file describing the model to be
                            trained

    optional arguments:
      -h, --help            show this help message and exit
      -s SERIALIZATION_DIR, --serialization-dir SERIALIZATION_DIR
                            directory in which to save the model and its logs
      -r, --recover         recover training from the state in serialization_dir
      -f, --force           overwrite the output directory if it exists
      -o OVERRIDES, --overrides OVERRIDES
                            a JSON structure used to override the experiment
                            configuration
      --file-friendly-logging
                            outputs tqdm status on separate lines and slows tqdm
                            refresh rate
      --cache-directory CACHE_DIRECTORY
                            Location to store cache of data preprocessing
      --cache-prefix CACHE_PREFIX
                            Prefix to use for data caching, giving current
                            parameter settings a name in the cache, instead of
                            computing a hash
      --include-package INCLUDE_PACKAGE
                            additional packages to include
"""

import argparse
import copy
import datetime
import logging
import os
import re
from typing import Dict, List, Union

from allennlp.commands.train import train_model, Train
from allennlp.common import Params
from allennlp.models.model import Model
from polyaxon_client.tracking import Experiment

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name

# There is a reason I create experiment on the module level. The metric event handler requires `Trainer` object.
# Current implementation of Trainer doesn't allow to pass any optional arguments **kwargs since every parameter is read
# from config file.
experiment = Experiment()


class TrainPolyaxon(Train):

    # I wanted the parser to be the same as for `Train` subcommand. Polyaxon doesn't require to pass argument
    # --serialization_dir, but in `Train` subcommand it is required. I could either make it optional and use
    # `experiment.get_outputs_path()` inside code or leave the parser as it is and make the user pass
    # $POLYAXON_RUN_OUTPUTS_PATH if Polyaxon is used. I decided on the second approach.
    def add_subparser(self, name: str, parser: argparse._SubParsersAction) -> argparse.ArgumentParser:
        subparser = super().add_subparser(name, parser)
        subparser.description = '''Train the specified model on the specified dataset in the Polyaxon environment.'''

        subparser.set_defaults(func=TrainPolyaxon.train_model_from_args)
        return subparser

    @staticmethod
    def flatten_params(params: Dict):
        out = {}

        def flatten(root: Union[Dict, List, str, bool, int, float], name: str = ''):
            if isinstance(root, dict):
                # I decided not to wrap `type` attribute, because:
                # 1) Polyaxon adds additional params whilst HP tuning by default. As the result there is redundancy
                #    in params e.g. `trainer.optimizer.lr` and `trainer.callback.optimizer.adam.lr`.
                # 2) I can easily compare e.g. learning rate across different optimizers.
                #
                # if 'type' in root:
                #     object_type = root.pop('type')
                #     name += object_type + '.'
                #
                #     if len(root) == 0:
                #         flatten('', name)

                for key, value in root.items():
                    flatten(value, name + key + '.')
            elif isinstance(root, list):
                for idx, value in enumerate(root):
                    flatten(value, name + str(idx) + '.')
            else:
                name = name[:-1]  # Remove last dot
                out[name] = root

        # Pop changes the input params
        params = copy.deepcopy(params)
        flatten(params)

        return out

    @staticmethod
    def convert_str_elapsed_time(elapsed_time: str) -> float:
        """
        Polyaxon cannot handle string in the reported metrics, therefore I need to convert elapsed time into a number.
        I decided to return value in hours given the data and GPU resources.
        """
        pattern = re.search(r'^(?:(\d+) day[s]?, )?(\d{1,2}):(\d{2}):(\d{2})(?:.(\d+))?$', elapsed_time)
        if pattern is None:
            raise ValueError('Incorrect elapsed time. Perhaps wrong implementation or change in datetime.deltatime')

        days, hours, minutes, seconds, milliseconds = pattern.groups()
        elapsed_timedelta = datetime.timedelta(
            days=0 if days is None else int(days),
            hours=0 if hours is None else int(hours),
            minutes=0 if minutes is None else int(minutes),
            seconds=0 if seconds is None else int(seconds),
            milliseconds=0 if milliseconds is None else int(milliseconds)
        )

        return elapsed_timedelta / datetime.timedelta(hours=1)

    @staticmethod
    def train_model_from_args(args: argparse.Namespace):
        """
        Just converts from an ``argparse.Namespace`` object to string paths.
        """
        TrainPolyaxon.train_model_from_file(args.param_path,
                                            args.serialization_dir,
                                            args.overrides,
                                            args.file_friendly_logging,
                                            args.recover,
                                            args.force,
                                            args.cache_directory,
                                            args.cache_prefix)

    @staticmethod
    def train_model_from_file(parameter_filename: str,
                              serialization_dir: str,
                              overrides: str = "",
                              file_friendly_logging: bool = False,
                              recover: bool = False,
                              force: bool = False,
                              cache_directory: str = None,
                              cache_prefix: str = None) -> Model:
        """
        A wrapper around :func:`train_model` which loads the params from a file.

        Parameters
        ----------
        parameter_filename : ``str``
            A json parameter file specifying an AllenNLP experiment.
        serialization_dir : ``str``
            The directory in which to save results and logs. We just pass this along to
            :func:`train_model`.
        overrides : ``str``
            A JSON string that we will use to override values in the input parameter file.
        file_friendly_logging : ``bool``, optional (default=False)
            If ``True``, we make our output more friendly to saved model files.  We just pass this
            along to :func:`train_model`.
        recover : ``bool`, optional (default=False)
            If ``True``, we will try to recover a training run from an existing serialization
            directory.  This is only intended for use when something actually crashed during the middle
            of a run.  For continuing training a model on new data, see the ``fine-tune`` command.
        force : ``bool``, optional (default=False)
            If ``True``, we will overwrite the serialization directory if it already exists.
        cache_directory : ``str``, optional
            For caching data pre-processing.  See :func:`allennlp.training.util.datasets_from_params`.
        cache_prefix : ``str``, optional
            For caching data pre-processing.  See :func:`allennlp.training.util.datasets_from_params`.
        """

        # Note, using `ext_vars` mechanism in jsonnet is not a good idea to pass params, since you will lost types.
        # Jsonnet doesn't support `parseDouble` (https://jsonnet.org/ref/stdlib.html) => all `std.extVar` are strings.

        # I need to pop (not get!), because `_jsonnet.evaluate_file()` or `_jsonnet.evaluate_snippet()` in AllenNLP
        # will crash. It's because they accept mapping like str -> str only (https://jsonnet.org/ref/bindings.html),
        # but env $POLYAXON_PARAMS doesn't contain strings only, but many different types e.g. '{"lr": 0.987}.'
        polyaxon_params = os.environ.pop('POLYAXON_PARAMS', None)
        logger.info(f'Detected environmental variable $POLYAXON_PARAMS={polyaxon_params}')

        # Polyaxon return weirdly 'null' string for a simple experiment (not hyperparameter tuning)
        polyaxon_params = None if polyaxon_params == 'null' else polyaxon_params
        if polyaxon_params is not None:
            overrides = polyaxon_params
            logger.warning('Ignoring `--overrides` argument, because $POLYAXON_PARAMS was detected.')

        # Load the experiment config from a file and pass it to ``train_model``.
        params = Params.from_file(parameter_filename, overrides)

        # Log parameters to Polyaxon. Note that `params.as_flat_dict()` doesn't handle list of dicts.
        flatten_params = TrainPolyaxon.flatten_params(params.params)
        experiment.log_params(**flatten_params)

        # Polyaxon doesn't allow to calculate data refs on file streams, therefore I need to read the whole file
        # into the memory.
        if 'train_data_path' in params:
            with open(params['train_data_path'], 'rb') as f:
                content = f.read()
                experiment.log_data_ref(content, 'train')
        if 'validation_data_path' in params:
            with open(params['validation_data_path'], 'rb') as f:
                content = f.read()
                experiment.log_data_ref(content, 'validation')

        model = train_model(params,
                            serialization_dir,
                            file_friendly_logging,
                            recover,
                            force,
                            cache_directory,
                            cache_prefix)

        return model
