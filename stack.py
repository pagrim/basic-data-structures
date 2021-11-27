from linked_list import LinkedList

class Stack:

    def __init__(self, data=None):
        self.linked_list = LinkedList(data)

    def __repr__(self):
        return self.linked_list.__repr__()

    def pop(self):
        val = self.linked_list.get_last()
        self.linked_list.remove_last()
        return val

    def push(self, value):
        self.linked_list.add_last(value)

    def top(self):
        return self.linked_list.get_last().get_value()

    def top_left(self):
        return self.linked_list.get_first().get_value()

    def is_empty(self):
        return len(self.linked_list) == 0
