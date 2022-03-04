import struct

import gdb
import pytest

import gdbp

TEST_VARIABLE_NAME = 'test_variable'
TEST_VARIABLE_ADDRESS = 0x08000000
TEST_VARIABLE_BYTES = struct.pack('=Q', 0xF123456789ABCDEF)


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    gdb.execute('break main')
    gdb.execute('r')
    yield
    gdb.execute('delete breakpoints')


def test_get_symbol_address():
    assert gdbp.get_symbol_address(TEST_VARIABLE_NAME) == TEST_VARIABLE_ADDRESS


def test_read_bytes():
    assert gdbp.read_bytes(TEST_VARIABLE_ADDRESS, len(TEST_VARIABLE_BYTES)) == TEST_VARIABLE_BYTES


def test_read_int8u():
    assert gdbp.read_int8u(TEST_VARIABLE_ADDRESS) == struct.unpack_from('B', TEST_VARIABLE_BYTES)[0]


def test_read_int8s():
    assert gdbp.read_int8s(TEST_VARIABLE_ADDRESS) == struct.unpack_from('b', TEST_VARIABLE_BYTES)[0]


def test_read_int16u():
    assert gdbp.read_int16u(TEST_VARIABLE_ADDRESS) == struct.unpack_from('=H', TEST_VARIABLE_BYTES)[0]


def test_read_int16s():
    assert gdbp.read_int16s(TEST_VARIABLE_ADDRESS) == struct.unpack_from('=h', TEST_VARIABLE_BYTES)[0]


def test_read_int16ub():
    assert gdbp.read_int16ub(TEST_VARIABLE_ADDRESS) == struct.unpack_from('>H', TEST_VARIABLE_BYTES)[0]


def test_read_int16sb():
    assert gdbp.read_int16sb(TEST_VARIABLE_ADDRESS) == struct.unpack_from('>h', TEST_VARIABLE_BYTES)[0]


def test_read_int16ul():
    assert gdbp.read_int16ul(TEST_VARIABLE_ADDRESS) == struct.unpack_from('<H', TEST_VARIABLE_BYTES)[0]


def test_read_int16sl():
    assert gdbp.read_int16sl(TEST_VARIABLE_ADDRESS) == struct.unpack_from('<h', TEST_VARIABLE_BYTES)[0]


def test_read_int32u():
    assert gdbp.read_int32u(TEST_VARIABLE_ADDRESS) == struct.unpack_from('=L', TEST_VARIABLE_BYTES)[0]


def test_read_int32s():
    assert gdbp.read_int32s(TEST_VARIABLE_ADDRESS) == struct.unpack_from('=l', TEST_VARIABLE_BYTES)[0]


def test_read_int32ub():
    assert gdbp.read_int32ub(TEST_VARIABLE_ADDRESS) == struct.unpack_from('>L', TEST_VARIABLE_BYTES)[0]


def test_read_int32sb():
    assert gdbp.read_int32sb(TEST_VARIABLE_ADDRESS) == struct.unpack_from('>l', TEST_VARIABLE_BYTES)[0]


def test_read_int32ul():
    assert gdbp.read_int32ul(TEST_VARIABLE_ADDRESS) == struct.unpack_from('<L', TEST_VARIABLE_BYTES)[0]


def test_read_int32sl():
    assert gdbp.read_int32sl(TEST_VARIABLE_ADDRESS) == struct.unpack_from('<l', TEST_VARIABLE_BYTES)[0]


def test_read_int64u():
    assert gdbp.read_int64u(TEST_VARIABLE_ADDRESS) == struct.unpack_from('=Q', TEST_VARIABLE_BYTES)[0]


def test_read_int64s():
    assert gdbp.read_int64s(TEST_VARIABLE_ADDRESS) == struct.unpack_from('=q', TEST_VARIABLE_BYTES)[0]


def test_read_int64ub():
    assert gdbp.read_int64ub(TEST_VARIABLE_ADDRESS) == struct.unpack_from('>Q', TEST_VARIABLE_BYTES)[0]


def test_read_int64sb():
    assert gdbp.read_int64sb(TEST_VARIABLE_ADDRESS) == struct.unpack_from('>q', TEST_VARIABLE_BYTES)[0]


def test_read_int64ul():
    assert gdbp.read_int64ul(TEST_VARIABLE_ADDRESS) == struct.unpack_from('<Q', TEST_VARIABLE_BYTES)[0]


def test_read_int64sl():
    assert gdbp.read_int64sl(TEST_VARIABLE_ADDRESS) == struct.unpack_from('<q', TEST_VARIABLE_BYTES)[0]


exit_code = pytest.main(['--capture=no'])
gdb.execute('quit {}'.format(exit_code))
