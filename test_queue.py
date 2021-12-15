import pytest

from queue import Queue

@pytest.fixture
def mock_queue():
    return Queue([1, 2, 3])

def test_init(mock_queue):
    qu = Queue()
    for item in [1,2,3]:
        qu.push(item)
    assert qu == mock_queue

def test_pop(mock_queue):
    mock_queue.pop()
    mock_queue.pop()
    assert mock_queue == Queue([3])

def test_push(mock_queue):
    mock_queue.push(4)
    assert mock_queue == Queue([1, 2, 3, 4])
