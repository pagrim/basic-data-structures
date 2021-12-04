
class FullQueue(Exception):
    pass

class EmptyQueue(Exception):
    pass

class FixedQueue:

    def __init__(self, length, values=None):
        self.length = length
        self.buffer_size = 1
        self.total_length = length + self.buffer_size
        self.read = 0
        self.write = 0
        self.queue = [None] * self.total_length
        self._init_values(values)

    def __repr__(self):
        return 'FixedQueue(length={},values={})'.format(self.length, self.queue)

    def __eq__(self, other):
        same_length = self.length == other.length
        zipped = [z for z in zip(self.queue, other.queue)]
        same_values = [sv == ov for sv, ov in zipped]
        return same_length and all(same_values)

    def _init_values(self, values):
        if values is not None:
            assert len(values) <= self.length
            for val in values:
                self.enqueue(val)

    def top(self):
        return self.queue[self.read]

    def is_full(self):
        return (self.write + 1) % self.total_length == self.read

    def is_empty(self):
        return self.read == self.write

    def last_item(self):
        return self.queue[(self.write -1) % self.total_length]

    def enqueue(self, value):
        if self.is_full():
            raise FullQueue
        else:
            self.queue[self.write] = value
            self.write = (self.write + 1) % self.total_length

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue
        else:
            value = self.queue[self.read]
            self.queue[self.read] = None
            self.read = (self.read + 1) % self.total_length
            return value
