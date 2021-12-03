
class FullQueue(Exception):
    pass

class EmptyQueue(Exception):
    pass

class FixedQueue:

    def __init__(self, length, values=None):
        self.length = length
        self.read = 0
        self.write = 0
        self._init_values(values)

    def __eq__(self, other):
        same_length = self.length == other.length
        same_values = [sv == ov for sv, ov in zip(self.queue, other.queue)]
        return same_length and same_values

    def _init_values(self, values):
        self.queue = [None] * self.length
        if values is not None:
            assert len(values) < self.length
            for val in values:
                self.enqueue(val)

    def top(self):
        return self.queue[self.read]

    def is_full(self):
        return (self.write + 1) % self.length == self.read

    def is_empty(self):
        return self.read == self.write

    def enqueue(self, value):
        if self.is_full():
            raise FullQueue
        else:
            self.queue[self.write] = value
            self.write = (self.write + 1) % self.length

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue
        else:
            value = self.queue[self.read]
            self.queue[self.read] = None
            self.read = (self.read + 1) % self.length
            return value
