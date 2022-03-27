import struct

import gdb


def read_bytes(address, length):
    """
    :param int address: Address to read from
    :param int length: Number of bytes to read
    :return bytes: The first ``length`` bytes starting at ``address``
    """
    # gdb.Inferior.read_memory was added in GDB 7.2
    return bytes(gdb.selected_inferior().read_memory(address, length))


def read_int8u(address):
    """
    :param int address: Address of unsigned uint8
    :return int: Value of integer
    """
    return struct.unpack('B', read_bytes(address, 1))[0]


def read_int8s(address):
    """
    :param int address: Address of signed uint8
    :return int: Value of integer
    """
    return struct.unpack('b', read_bytes(address, 1))[0]


def read_int16u(address):
    """
    :param int address: Address of unsigned uint16, native endianness
    :return int: Value of integer
    """
    return struct.unpack('=H', read_bytes(address, 2))[0]


def read_int16s(address):
    """
    :param int address: Address of signed uint16, native endianness
    :return int: Value of integer
    """
    return struct.unpack('=h', read_bytes(address, 2))[0]


def read_int16ub(address):
    """
    :param int address: Address of unsigned uint16, big endian
    :return int: Value of integer
    """
    return struct.unpack('>H', read_bytes(address, 2))[0]


def read_int16sb(address):
    """
    :param int address: Address of signed uint16, big endian
    :return int: Value of integer
    """
    return struct.unpack('>h', read_bytes(address, 2))[0]


def read_int16ul(address):
    """
    :param int address: Address of unsigned uint16, little endian
    :return int: Value of integer
    """
    return struct.unpack('<H', read_bytes(address, 2))[0]


def read_int16sl(address):
    """
    :param int address: Address of signed uint16, little endian
    :return int: Value of integer
    """
    return struct.unpack('<h', read_bytes(address, 2))[0]


def read_int32u(address):
    """
    :param int address: Address of unsigned uint32, native endianness
    :return int: Value of integer
    """
    return struct.unpack('=L', read_bytes(address, 4))[0]


def read_int32s(address):
    """
    :param int address: Address of signed uint32, native endianness
    :return int: Value of integer
    """
    return struct.unpack('=l', read_bytes(address, 4))[0]


def read_int32ub(address):
    """
    :param int address: Address of unsigned uint32, big endian
    :return int: Value of integer
    """
    return struct.unpack('>L', read_bytes(address, 4))[0]


def read_int32sb(address):
    """
    :param int address: Address of signed uint32, big endian
    :return int: Value of integer
    """
    return struct.unpack('>l', read_bytes(address, 4))[0]


def read_int32ul(address):
    """
    :param int address: Address of unsigned uint32, little endian
    :return int: Value of integer
    """
    return struct.unpack('<L', read_bytes(address, 4))[0]


def read_int32sl(address):
    """
    :param int address: Address of signed uint32, little endian
    :return int: Value of integer
    """
    return struct.unpack('<l', read_bytes(address, 4))[0]


def read_int64u(address):
    """
    :param int address: Address of unsigned uint64, native endianness
    :return int: Value of integer
    """
    return struct.unpack('=Q', read_bytes(address, 8))[0]


def read_int64s(address):
    """
    :param int address: Address of signed uint64, native endianness
    :return int: Value of integer
    """
    return struct.unpack('=q', read_bytes(address, 8))[0]


def read_int64ub(address):
    """
    :param int address: Address of unsigned uint64, big endian
    :return int: Value of integer
    """
    return struct.unpack('>Q', read_bytes(address, 8))[0]


def read_int64sb(address):
    """
    :param int address: Address of signed uint64, big endian
    :return int: Value of integer
    """
    return struct.unpack('>q', read_bytes(address, 8))[0]


def read_int64ul(address):
    """
    :param int address: Address of unsigned uint64, little endian
    :return int: Value of integer
    """
    return struct.unpack('<Q', read_bytes(address, 8))[0]


def read_int64sl(address):
    """
    :param int address: Address of signed uint64, little endian
    :return int: Value of integer
    """
    return struct.unpack('<q', read_bytes(address, 8))[0]
