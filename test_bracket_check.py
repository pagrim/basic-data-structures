import pytest
from bracket_check import BracketChecker


@pytest.mark.parametrize(("in_str", "exp_res"), [
    ("[]", "success"),
    ("{}[]", "success"),
    ("[()]", "success"),
    ("(())", "success"),
    ("{[]}()", "success"),
    ("{", 1),
    ("{[}", 3),
    ("foo(bar);", "success"),
    ("foo(bar[i);", 10),
])
def test_check_brackets(in_str, exp_res):
    bc = BracketChecker(in_str)
    assert bc.check() == exp_res
