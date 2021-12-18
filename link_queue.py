from linked_list import LinkedList

class LinkQueue():

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
