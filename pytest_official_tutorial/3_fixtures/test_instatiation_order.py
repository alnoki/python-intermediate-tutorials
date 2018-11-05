import pytest


@pytest.fixture(scope="session")
def s1():
    pass


@pytest.fixture(scope="module")
def m1():
    pass


@pytest.fixture
def f1(tmpdir):
    pass


@pytest.fixture
def f2():
    pass


def test_foo(f1, m1, f2, s1):
    ...
