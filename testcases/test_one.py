import pytest


@pytest.mark.p0
def test_one():
    expect = 1
    actural = 1
    assert expect == actural

@pytest.mark.test
def test_two():
    expect = 2
    actural = 2
    assert expect == actural

