from stack import Stack, StackMinMax

import logging
logger = logging.getLogger()


class SlidingWindow():

    def __init__(self, window_size):
        self.s1 = StackMinMax()
        self.s2 = Stack()
        self.window_size = window_size

    def calculate(self, data):
        num_data = len(data)
        results = []
        for i in range(num_data):
            self.enqueue(data[i])
            if i >= self.window_size - 1:
                min_max = self.get_min_max()
                results.append(min_max)
        return results

    def enqueue(self, value):
        logger.debug('Enqueing: %s', value)
        self.log_stacks()
        # Pop the top of the stack to remove front of the queue
        if not self.s1.is_empty() and len(self.s1) >= self.window_size:
            self.s1.pop()
        # For each remaining value in the stack move to stack 2
        for _ in range(self.window_size - 1):
            if self.s1.is_empty():
                break
            else:
                val = self.s1.pop()
                self.s2.push(val)
        logger.debug('Moved values')
        self.log_stacks()
        # Put the new value on stack 1
        self.s1.push(value)
        logger.debug('Added value')
        self.log_stacks()
        # Move the values on stack 2 back
        while not self.s2.is_empty():
            val = self.s2.pop()
            self.s1.push(val)
        logger.debug('Replaced values')
        self.log_stacks()

    def get_min_max(self):
        return self.s1.get_min(), self.s1.get_max()

    def log_stacks(self):
        logger.debug('s1: %s', self.s1)
        logger.debug('s2: %s', self.s2)
