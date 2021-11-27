# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'{self.val}'

    def __eq__(self, other):
        return self.same_value(self, other) and self.same_value(self.next, other.next) and self.same_value(self.prev,
                                                                                                           other.prev)

    @staticmethod
    def same_value(first, second):
        if first is None:
            is_equal = second is None
        elif second is None:
            is_equal = first is None
        else:
            is_equal = first.val == second.val
        return is_equal

    def get_value(self):
        return self.val


class LinkedList():
    def __init__(self, nodes=None):
        if nodes is not None:
            print('Nodes of type', type(nodes), nodes)
            node = ListNode(val=nodes.pop(0))
            self.head = node
            prev_node = None
            for elem in nodes:
                node.next = ListNode(val=elem, prev=node)
                node.prev = prev_node
                prev_node = node
                node = node.next
            self.tail = node
        else:
            self.head = None
            self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        return len([val for val in self])

    def __eq__(self, other):
        try:
            assert len(self) == len(other)
        except AssertionError:
            print('LinkedList objects have different length')
            return False
        equalities = [sn == on for sn, on in zip(self, other)]
        return all(equalities)

    def add_first(self, value):
        node = ListNode(val=value, next=self.head, prev=None)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def add_last(self, value):
        if self.head is None:
            self.head = ListNode(val=value)
            self.tail = self.head
        else:
            last_node = ListNode(val=value, prev=self.tail)
            self.tail.next = last_node
            self.tail = last_node

    def remove_first(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def remove_last(self):
        if self.tail is None:
            pass
        elif self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def get_last(self):
        return self.tail

    def get_first(self):
        return self.head

    def __repr__(self):
        return ' -> '.join([node.__repr__() for node in self])
