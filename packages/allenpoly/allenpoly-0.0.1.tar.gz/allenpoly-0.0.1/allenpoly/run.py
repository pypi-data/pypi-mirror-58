#!/usr/bin/env python
import logging
import os
import sys

from allennlp.commands import main  # pylint: disable=wrong-import-position

from allenpoly.commands import TrainPolyaxon

if os.environ.get("ALLENNLP_DEBUG"):
    LEVEL = logging.DEBUG
else:
    LEVEL = logging.INFO

sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    level=LEVEL)


subcommand_overrides = {
    "train": TrainPolyaxon(),
}


def run():
    main(prog="allennlp", subcommand_overrides=subcommand_overrides)


if __name__ == "__main__":
    run()
