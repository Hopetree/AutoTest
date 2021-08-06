import pytest


@pytest.fixture(scope='module')
def conf():
    config = {
        "version": "0.1.0"
    }
    return config
