import pytest

from stack import Stack, StackMinMax

@pytest.fixture
def mock_stack():
    return Stack([1, 2, 3])

@pytest.fixture
def mock_stack_min_max():
    return StackMinMax([3, 2])


def test_init(mock_stack):
    stk = Stack()
    for item in [1,2,3]:
        stk.push(item)
    assert stk == mock_stack


def test_min_max(mock_stack_min_max):
    assert mock_stack_min_max.get_max() == 3
    assert mock_stack_min_max.get_min() == 2
    mock_stack_min_max.push(4)
    assert mock_stack_min_max.get_max() == 4
    mock_stack_min_max.pop()
    mock_stack_min_max.pop()
    assert mock_stack_min_max.get_min() == 3
    mock_stack_min_max.push(1)
    assert mock_stack_min_max.get_min() == 1
    assert mock_stack_min_max.get_max() == 3
