import gdb
import pytest


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    gdb.execute('break main')
    gdb.execute('r')
    yield
    gdb.execute('delete breakpoints')
