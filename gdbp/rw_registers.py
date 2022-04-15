import gdb


class GdbpInvalidRegister(RuntimeError):
    pass


def read_register(register_name):
    """
    :param str register_name: A valid register name (according to GDB)
    :return int: The register's (unsigned) value in the selected frame
    """
    # gdb.parse_and_eval & gdb.TYPE_CODE_VOID were added in GDB 7.1
    # gdb.Frame.read_register was added in GDB 7.9, which is higher than the min supported version
    value_object = gdb.parse_and_eval('$' + register_name)
    if value_object.type.code == gdb.TYPE_CODE_VOID:
        raise GdbpInvalidRegister()

    register_size_in_bits = value_object.type.sizeof * 8

    value = int(value_object)
    if value < 0:
        value += 2 ** register_size_in_bits

    return value


def write_register(register_name, value):
    """
    :param str register_name: A valid register name (according to GDB)
    :param int value: Value to write to register
    """
    # Verify that the register is readable
    read_register(register_name)

    # gdb.execute was added in GDB 7.0
    gdb.execute('set ${register_name} = {value}'.format(register_name=register_name, value=value))
