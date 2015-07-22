from unittest import TestCase
from experimentSuite.schedule import ExperimentSchedule
from experimentSuite.expstep import DummyExperimentStep

__author__ = 'martin'


class TestExperimentSchedule(TestCase):
    def setUp(self):
        tags = ["one", "two", "three"]
        self.dummy_steps = [DummyExperimentStep(x) for x in tags]
        self.experiment_schedule = ExperimentSchedule(self.dummy_steps)

    def test_next(self):
        experiment_step_sequence = list(self.experiment_schedule)
        self.assertSequenceEqual(experiment_step_sequence, self.dummy_steps)






