import pytest

from linked_list import ListNode, LinkedList


@pytest.fixture
def mock_ll():
    return LinkedList([1, 2, 3])


def test_same_value():
    assert (ListNode.same_value(ListNode(0), ListNode(0)))


def test_node_equality():
    n1 = ListNode(0)
    n2 = ListNode(0)
    n3 = ListNode(0)
    n3.next = ListNode(1)
    n4 = ListNode(1)
    n5 = ListNode(1)
    assert (n1 == n2 and n3 != n1 and n4 == n5 and n3 != n4)


def test_add_first(mock_ll):
    mock_ll.add_first(0)
    other = LinkedList([0, 1, 2, 3])
    assert (mock_ll == other and other.head == mock_ll.head)


def test_add_last(mock_ll):
    mock_ll.add_last(4)
    other = LinkedList([1, 2, 3, 4])
    assert (mock_ll == other and other.tail == mock_ll.tail)


def test_remove_first(mock_ll):
    mock_ll.remove_first()
    other = LinkedList([2, 3])
    assert (mock_ll == other and other.head == mock_ll.head)


def test_remove_last(mock_ll):
    mock_ll.remove_last()
    other = LinkedList([1, 2])
    assert (mock_ll == other and other.tail == mock_ll.tail)


def test_remove_last_single(mock_ll):
    for _ in range(3):
        mock_ll.remove_last()
    other = LinkedList()
    assert (mock_ll == other)


def test_empty():
    ll = LinkedList()
    ll.add_last(1)
    ll.add_first(2)
    assert (ll == LinkedList([2, 1]))


def test_len(mock_ll):
    assert (len(mock_ll) == 3)
