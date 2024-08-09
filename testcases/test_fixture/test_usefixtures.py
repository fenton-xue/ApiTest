# def test_usefixtures(use_fixtures):
#     print("usefixtures")
import pytest


@pytest.mark.usefixtures("use_fixtures")
def test_usefixtures():
    print("usefixtures")
