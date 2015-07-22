__author__ = 's_schmar'
import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class ExperimentSuite(object):

    def __init__(self, storage, experiment_schedule):
        """

        :param storage: dict
        :param experiment_schedule: experimentSuite.schedule.ExperimentSchedule
        """
        self.storage = storage
        self.experiment_schedule = experiment_schedule

    def run(self, **kwargs):
        """

        :param kwargs: named args passed to run method of experiment steps
        """
        try:
            schedule_iterator = iter(self.experiment_schedule)
            for experiment_step in schedule_iterator:
                experiment_step.run(self.storage, self.experiment_schedule, **kwargs)
        except StopExperimentException as e:
            log.info(e.message)

class StopExperimentException(Exception):
    pass


