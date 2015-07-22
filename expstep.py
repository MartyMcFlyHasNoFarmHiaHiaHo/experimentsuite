__author__ = 's_schmar'
from abc import ABCMeta, abstractmethod

class AbstractExperimentStep(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def run(self, storage, schedule):
        """

        :param storage: dict like object
        :param schedule: experimentSuite.schedule.ExperimentSchedule
        """
        pass

class DummyExperimentStep(AbstractExperimentStep):

    def __init__(self, tag):
        self.tag = tag

    def run(self, storage, schedule):
        print "Dummy {0} run".format(self.tag)
