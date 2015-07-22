from unittest import TestCase
from experimentSuite.suite import ExperimentSuite
from experimentSuite.schedule import ExperimentSchedule
from experimentSuite.expstep import DummyExperimentStep

__author__ = 'martin'

class TestExperimentSuite(TestCase):
    def setUp(self):
        tags = ["one", "two", "three"]
        self.dummy_steps = [DummyExperimentStep(x) for x in tags]
        self.experiment_schedule = ExperimentSchedule(self.dummy_steps)
        self.dummy_storage = {}
        self.experiment_suite = ExperimentSuite(self.dummy_storage, self.experiment_schedule)

    def modified_count_run(self, storage, schedule):
        if 'count' in storage:
            storage['count'] += 1
        else:
            storage['count'] = 1

    def augment_experiment_step_run(self):
        for experiment_step in self.dummy_steps:
            experiment_step.run = self.modified_count_run

    def test_run(self):
        self.augment_experiment_step_run()
        self.experiment_suite.run()
        self.assertEqual(self.dummy_storage['count'], len(self.dummy_steps))


