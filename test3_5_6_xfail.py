# @pytest.mark.xfail decoration is used to mark expected failing tests
# but if xfailing test unexpectedly passes, it may fail the test suite. 
# to prevent that it must be marked as failed anyway
# pytest -rX -v test3_5_6_xfail.py
# the result will be: 2 passed, 1 xpassed

import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False


