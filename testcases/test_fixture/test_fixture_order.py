import pytest


@pytest.fixture(scope="session")
def t_session():
    print("我是session fixture")


@pytest.fixture(scope="module")
def t_module():
    print("我是module fixture")


@pytest.fixture(scope="class")
def t_class():
    print("我是class fixture")


@pytest.fixture(scope="function")
def t_function():
    print("我是function fixture")


class TestFixtureOrder:
    def test_fixture_order(self, t_session, t_module, t_class, t_function):
        assert 1 == 1
