import pytest
from bracket_check import BracketChecker


@pytest.mark.parametrize(("in_str", "exp_res"), [
    ("[]", "Success"),
    ("{}[]", "Success"),
    ("[()]", "Success"),
    ("(())", "Success"),
    ("{[]}()", "Success"),
    ("{", 1),
    ("}", 1),
    ("{[}", 3),
    ("foo(bar);", "Success"),
    ("", "Success")
])
def test_check_brackets(in_str, exp_res):
    bc = BracketChecker(in_str)
    assert bc.check() == exp_res
