# pylint: disable=unused-variable,arguments-differ
from typing import TYPE_CHECKING

from allennlp.training.callbacks import TrackMetrics
from allennlp.training.callbacks.callback import Callback, handle_event
from allennlp.training.callbacks.events import Events

from allenpoly.commands import experiment  # Be careful with top-level variable!

if TYPE_CHECKING:
    from allennlp.training.callback_trainer import CallbackTrainer  # pylint:disable=unused-import


@TrackMetrics.register("poly_track_metrics")
class PolyTrackMetrics(TrackMetrics):
    """ TrackMetrics wrapper that additionally logs metrics into Polyaxon dashboard. """

    def __init__(self, patience: int = None, validation_metric: str = "-loss"):
        super().__init__(patience, validation_metric)

    # Requires low priority, because TrackMetrics has to first fill in `trainer.metrics`
    @handle_event(Events.EPOCH_END, priority=-100)
    def poly_end_of_epoch(self, trainer: 'CallbackTrainer'):
        metrics = {}
        for key, value in trainer.train_metrics.items():
            metrics["training_" + key] = value

        for key, value in trainer.val_metrics.items():
            metrics["validation_" + key] = value

        # I am not interested in collecting, but `track_metrics` does it automatically
        metrics = {name: value for name, value in metrics.items() if 'memory' not in name}
        experiment.log_metrics(step=trainer.epoch_number, **metrics)

    # Allows to easily compare experiment against the best validation score in Polyaxon after training.
    @handle_event(Events.TRAINING_END, priority=-100)
    def poly_end_of_training(self, trainer: 'CallbackTrainer'):
        metrics = {name: value for name, value  in trainer.metrics.items() if 'best_validation_' in name}
        metrics['best_step'] = trainer.metrics['best_epoch']
        experiment.log_metrics(**metrics)
