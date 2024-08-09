import pytest


@pytest.fixture(scope="session")
def test_session():
    print("我是session级的fixture")


@pytest.fixture(scope="function", autouse=True)
def test_func1():
    print("我是func1级别的fixture")


@pytest.fixture(scope="function", autouse=True)
def test_func2():
    print("我是func2级别的fixture")


@pytest.fixture(scope="function")
def get_params():
    return {"shouji": "1234567890", "appkey": "1234567890"}


@pytest.fixture(scope="function", autouse=True)
def fun():
    print("\n我是前置步骤")
    yield
    print("我是后置步骤")

@pytest.fixture(scope="function")
def use_fixtures():
    print("我现在使用usefixtures")
