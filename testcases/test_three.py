import pytest


@pytest.mark.pro
class TestThree:

    def test_one(self):
        expect = 1
        actural = 1
        assert expect == actural

    def test_two(self):
        expect = 2
        actural = 2
        assert expect == actural
