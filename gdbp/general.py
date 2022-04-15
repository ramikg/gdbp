import gdb


def get_symbol_address(symbol):
    """
    :param str symbol: The symbol's name
    :return int: The symbol's address
    """
    # gdb.lookup_symbol was added in GDB 7.2
    symbol_object = gdb.lookup_symbol(symbol)[0]
    if symbol_object:
        return int(symbol_object.value().address)
    else:
        # Workaround for non-debugging symbols
        value_object = gdb.parse_and_eval('&' + symbol)
        return int(value_object)
