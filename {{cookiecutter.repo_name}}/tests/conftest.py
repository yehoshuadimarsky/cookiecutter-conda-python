import pytest


@pytest.fixture(scope='session')
def session_fixture():
    print('a session fixture goes here!')
