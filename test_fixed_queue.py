from fixed_queue import FixedQueue
import pytest

@pytest.fixture
def mock_queue():
    return FixedQueue(length=5, values=['A', 'B', 'C', 'D'])


def test_enqueue():
    fq = FixedQueue(length=3)
    print(fq.queue)
    fq.enqueue('A')
    fq.enqueue('B')
    assert fq == FixedQueue(length=3, values=['A', 'B'])


def test_dequeue(mock_queue):
    first = mock_queue.dequeue()
    second = mock_queue.dequeue()
    assert first == 'A' and second == 'B' and mock_queue.top() == 'C'


def test_full(mock_queue):
    mock_queue.enqueue('E')
    assert mock_queue.is_full()


def test_empty():
    fq = FixedQueue(length=4)
    fq.enqueue('A')
    fq.dequeue()
    assert fq.is_empty()

def test_last_item(mock_queue):
    initial_last = mock_queue.last_item()
    mock_queue.dequeue()
    mock_queue.dequeue()
    mock_queue.enqueue('E')
    mock_queue.enqueue('F')
    final_last = mock_queue.last_item()
    assert initial_last == 'D' and final_last == 'F'
