from unittest import TestCase
from experimentSuite.iterator import ExperimentIterator

__author__ = 'martin'


class TestExperimentIterator(TestCase):
    def setUp(self):
        import ipdb
        ipdb.set_trace()
        self.elements = [1, 2, 3, 4, 5]
        self.experiment_iterator = ExperimentIterator(self.elements)

    def test_next(self):
        iterator_sequence = list(self.experiment_iterator)
        self.assertSequenceEqual(iterator_sequence, self.elements)

