import pytest


@pytest.fixture(params=["str1", "str2"], ids=["case1", "case2"])
def params_fixture(request):
    return request.param


def test_params(params_fixture):
    print(params_fixture)

