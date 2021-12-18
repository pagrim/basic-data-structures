from sliding_window import SlidingWindow
from stack import Stack, StackMinMax

import pytest

@pytest.fixture
def mock_sw_4():
    return SlidingWindow(window_size=4)

@pytest.fixture
def mock_sw_2():
    return SlidingWindow(window_size=2)


def test_enqueue_1(mock_sw_2):
    mock_sw_2.enqueue(1)
    mock_sw_2.enqueue(2)
    mock_sw_2.enqueue(3)
    assert mock_sw_2.s1 == StackMinMax(data=[3, 2])


def test_calculate(mock_sw_4):
    input_data = [2, 7, 3, 1, 5, 2, 6, 2]
    exp_min_max = [(1, 7), (1, 7), (1,5), (1, 6), (2, 6)]
    assert mock_sw_4.calculate(input_data) == exp_min_max
