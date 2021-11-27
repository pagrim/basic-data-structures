import pytest
from bracket_check import BracketChecker


@pytest.fixture
def example_successes():
    return ['[]', '{}[]', '[()]', '(())', '{[]}()']


def test_successes(example_successes):
    assert all([BracketChecker(example).check() == 'success' for example in example_successes])
