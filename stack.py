from linked_list import LinkedList
import sys

class Stack:

    def __init__(self, data=None):
        self.linked_list = LinkedList()
        if data is not None:
            for item in data:
                self.push(item)

    def __repr__(self):
        return self.linked_list.__repr__()

    def __eq__(self, other):
        return self.linked_list == other.linked_list

    def __len__(self):
        return len(self.linked_list)

    def pop(self):
        val = self.linked_list.get_last()
        self.linked_list.remove_last()
        return val

    def push(self, value):
        self.linked_list.add_last(value)

    def get_min(self):
        return self.min_list.get_last()

    def top(self):
        return self.linked_list.get_last()

    def top_left(self):
        return self.linked_list.get_first()

    def is_empty(self):
        return len(self.linked_list) == 0

class StackMinMax:

    def __init__(self, data=None):
        self.stack = Stack()
        self.max_stack = Stack()
        self.min_stack = Stack()
        if data is not None:
            for item in data:
                self.push(item)

    def __eq__(self, other):
        return self.stack == other.stack and self.max_stack == other.max_stack and self.min_stack == other.min_stack

    def __repr__(self):
        return ",".join([f"{k}:{v}" for k, v in self.__dict__.items()])

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        self.stack.push(value)
        curr_max = self.get_max()
        curr_min = self.get_min()
        if value > curr_max:
            self.max_stack.push(value)
        else:
            self.max_stack.push(curr_max)
        if value < curr_min:
            self.min_stack.push(value)
        else:
            self.min_stack.push(curr_min)

    def pop(self):
        self.max_stack.pop()
        self.min_stack.pop()
        return self.stack.pop()

    def get_max(self):
        top = self.max_stack.top()
        if top is None:
            max_val = -sys.maxsize
        else:
            max_val = top
        return max_val

    def get_min(self):
        top = self.min_stack.top()
        if top is None:
            min_val = sys.maxsize
        else:
            min_val = top
        return min_val

    def is_empty(self):
        return self.stack.is_empty()
