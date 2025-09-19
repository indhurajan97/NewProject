import pytest

@pytest.fixture(scope='session')
def prework():
    print("Browser instance")