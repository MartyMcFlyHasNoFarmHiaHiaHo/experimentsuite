__author__ = 'martin'

import logging
from datastructures import PriorityQueue
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class ExperimentIterator(object):

    def __init__(self, elements):
        """

        :param elements: list
        """
        self.pq = PriorityQueue()
        map(lambda (i, elem): self.pq.push(elem, i), enumerate(reversed(elements)))

    def next(self):
        try:
            return self.pq.pop()
        except:
            raise StopIteration

    def __iter__(self):
        return self


