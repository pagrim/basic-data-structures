from linked_list import LinkedList

class Queue():

    def __init__(self, data=None):
        self.linked_list = LinkedList()
        if data is not None:
            for item in data:
                self.push(item)

    def __repr__(self):
        return self.linked_list.__repr__()

    def __eq__(self, other):
        return self.linked_list == other.linked_list

    def pop(self):
        val = self.linked_list.get_first()
        self.linked_list.remove_first()
        return val

    def push(self, value):
        self.linked_list.add_last(value)

    def get_min(self):
        return self.min_list.get_last()

    def top(self):
        return self.linked_list.get_first()

    def top_right(self):
        return self.linked_list.get_last()

    def is_empty(self):
        return len(self.linked_list) == 0

class QueueWithWindowMinMax():

    def __init__(self, window_size):
        self.queue = Queue()
        self.min_queue = Queue()
        self.max_queue = Queue()
        self.window_size = window_size

    def calculate(self, data):
        num_data = len(data)
        last_sliding_value = num_data - self.window_size + 1
        min_vals = []
        max_vals = []
        for i in range(last_sliding_value):
            min_val, max_val = self.sliding_push(data[i])
            if min_val is not None:
                min_vals.append(min_val)
            if max_val is not None:
                max_vals.append(max_val)

    def sliding_push(self, value):
        if len(self.queue) >= self.window_size:
            self.push_all(value)
            self.pop_all()
            max_val = self.max_queue.top()
            min_val = self.min_queue.top()
        else:
            self.push_all()
            max_val = None
            min_val = None
        return max_val, min_val

    def push_all(self, value):
        curr_max = self.max_queue.top()
        curr_min = self.min_queue.top()
        if value >= curr_max:
            self.queue.push(value)
            self.max_queue.push(value)
        else:
            self.queue.push(value)
            self.max_queue.push(curr_max)
        if value <= curr_min:
            self.queue.push(value)
            self.min_queue.push(value)
        else:
            self.queue.push(value)
            self.min_queue.push(curr_min)

    def pop_all():
        self.queue.pop()
        self.min_queue.pop()
        self.max_queue.pop()
