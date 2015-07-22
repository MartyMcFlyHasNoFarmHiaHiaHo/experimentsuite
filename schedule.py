__author__ = 'martin'
from iterator import ExperimentIterator

class ExperimentSchedule(object):

    def __init__(self, experiment_steps):
        """

        :param experiment_steps: list of experimentSuite.expstep.AbstractExperimentStep objects
        """
        self.experiment_steps = experiment_steps

    def assemble_iterator(self):
        experiment_iterator = ExperimentIterator(self.experiment_steps)
        return experiment_iterator

    def __iter__(self):
        return self.assemble_iterator()

