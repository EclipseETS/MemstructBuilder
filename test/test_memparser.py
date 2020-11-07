
import sys
import itertools
from board_mod import Board
from message_mod import Message
from signal_mod import Signal
from memparser import *


def test_get_signal_from_entry():
    # Test signal parsing
    # Signal format :
    # s:<Signal Name>, <Type>, <Init Value>, <Factor>, <Offset>, <Unit>, <Min Value>, <Max Value>
    # Supported types : 8, 16, 32, U8, U16, U32, F

    # To add a test case, simply add a value to the following tables :
    names_to_test = ['NAME']
    ids_to_test = [0x100, 0x200]
    types_to_test = ['8', '16', '32', 'U8', 'U16', 'U32', 'F']  # Test signed, unsigned and floating types
    init_values_to_test = [0, 10]
    factors_to_test = [1, 3.75]
    offsets_to_test = [0, 100]
    units_to_test = ['RPM']
    min_values_to_test = [0]
    max_values_to_test = [1000]
    values_to_test = itertools.product(names_to_test, ids_to_test, types_to_test, init_values_to_test, factors_to_test,
                                       offsets_to_test, units_to_test, min_values_to_test, max_values_to_test)

    # Mapping of type string (32, U32, F) to signal types (int32_t, float, etc..)
    types_dict = {'8': 'int8_t', '16': 'int16_t', '32': 'int32_t',
                  'U8': 'uint8_t', 'U16': 'uint16_t', 'U32': 'uint32_t',
                  'F': 'float'}
    # Mapping of type string (32, U32, F) to bitsizes
    bitsizes_dict = {'8': 8, 'U8': 8,
                     '16': 16, 'U16': 16,
                     '32': 32, 'U32': 32, 'F': 32}
    # Mapping of type string (32, U32, F) to signed bool
    signed_dict = {'8': 'true', '16': 'true', '32': 'true', 'F': 'true',
                   'U8': 'false', 'U16': 'false', 'U32': 'false'}

    index = 0
    for name, sigid, datatype, initvalue, factor, offset, unit, minvalue, maxvalue in values_to_test:
        sig = Signal()
        # The starting 's:' is removed by eclipseMemstructGen.py parsing
        raw_line = f'{name}, {datatype}, {initvalue}, {factor}, {offset}, {unit}, {minvalue}, {maxvalue}'
        get_signal_from_entry(raw_line, index, sigid, sig)
        index += 1

        # Test that parsing was successful
        assert sig.name == name
        assert sig.id == sigid
        assert sig.type == types_dict[datatype]
        assert sig.bitsize == bitsizes_dict[datatype]
        assert sig.float == ('true' if datatype == 'F' else 'false')
        assert sig.signed == signed_dict[datatype]
        assert sig.init_value == initvalue
        assert sig.factor == factor
        assert sig.offset == offset
        assert sig.unit == unit
        assert sig.minvalue == minvalue
        assert sig.maxvalue == maxvalue


def test_get_message_from_entry():
    # Test message parsing
    # Message format :
    # m:<Message Name>, <ID>

    # To add a test case, simply add a value to the tables :
    names_to_test = ['NAME']
    ids_to_test = [0x01, 0x10]
    values_to_test = itertools.product(names_to_test, ids_to_test)

    index = 0
    for name, message_id in values_to_test:
        message = Message()
        # The starting 'm:' has already been parsed by eclipseMemstructGen.py
        raw_line = '{}, {:#02x}'.format(name, message_id)
        get_message_from_entry(raw_line, index, message)
        index += 1

        # Test that the parsing was successful
        assert message.name == name
        assert message.id == message_id


def test_get_board_from_entry():
    # Test board parsing
    # Board format :
    # 'b:<Board Name>, <Offset>, <Extend>, <Endianness>'
    # Offset = ID, Extend = Bool for extended CAN, Endianness = 1 for little endian, 0 for big endian

    names_to_test = ['NAME']
    offsets_to_test = [0x0, 0x100]
    extends_to_test = [0, 1]  # 0 = standard CAN, 1 = extended CAN
    endianness_to_test = [0, 1]  # 0 = Big endian, 1 = little endian
    values_to_test = itertools.product(names_to_test, offsets_to_test, extends_to_test, endianness_to_test)

    index = 0
    for name, offset, extend, endianness in values_to_test:
        board = Board()
        # The starting 'b:' has already been parsed by eclipseMemstructGen.py
        offset_string = '{:#02x}'.format(offset)  # Formatting for hex ('0xAA')
        raw_line = f'{name}, {offset_string}, {extend}, {endianness}'
        get_board_from_entry(raw_line, index, board)
        index += 1

        # Test that parsing was successful
        assert board.name == name
        assert board.offset == offset
        assert board.extend == extend
        assert board.little_endian == endianness


def check_signal_report_error(capsys, name, datatype, init_value, factor, offset, unit_name, min_value, max_value):
    raw_line = f'{name}, {datatype}, {init_value}, {factor}, {offset}, {unit_name}, {min_value}, {max_value}'
    error_value = get_signal_from_entry(raw_line, 0, 0, Signal())
    out, err = capsys.readouterr()
    assert (out != '' and error_value == -1), \
        f'get_signal_from_entry() failed to print error with name = {name}, type = {datatype}, ' \
        f'init_value = {init_value}, factor = {factor}, offset = {offset}, ' \
        f'unit_name = {unit_name}, min value = {min_value}, max_value = {max_value}'


def test_invalid_arguments_get_signal_from_entry(capsys):
    # Test invalid length signal string
    raw_line = f'test, U32, 0, 0, 0, RPM, -100, 100, 0'
    error_value = get_signal_from_entry(raw_line, 0, 0, Signal())
    assert error_value is None or error_value == -1

    # Invalid characters like 'é' or '%'
    strings_to_test = ['%test%', '°test°', 'étesté', '-test-']
    for string in strings_to_test:
        check_signal_report_error(capsys, string, 'U32', 0, 0, 0, 'RPM', -100, 100)
        check_signal_report_error(capsys, 'test', 'U32', 0, 0, 0, string, -100, 100)

    # Test error reporting of a bad datatype
    types_to_test = ['U9', 'D', 'test']
    for datatype in types_to_test:
        check_signal_report_error(capsys, 'test', datatype, 0, 0, 0, 'RPM', -100, 100)

    # Test init values, factors, offsets, min_values and max_values that are not ints
    values = ['abc', True]
    for value in values:
        check_signal_report_error(capsys, 'test', 'U32', value, 0, 0, 'RPM', -100, 100)
        check_signal_report_error(capsys, 'test', 'U32', 0, value, 0, 'RPM', -100, 100)
        check_signal_report_error(capsys, 'test', 'U32', 0, 0, value, 'RPM', -100, 100)
        check_signal_report_error(capsys, 'test', 'U32', 0, 0, 0, 'RPM', value, 100)
        check_signal_report_error(capsys, 'test', 'U32', 0, 0, 0, 'RPM', -100, value)


def check_message_report_error(capsys, name, message_id):
    raw_line = f'{name}, {message_id}'
    error_value = get_message_from_entry(raw_line, 0, Message())
    out, err = capsys.readouterr()
    assert (out != '' and error_value == -1), \
        f'get_message_from_entry() failed to print error with name = {name} and id = {message_id}'


def test_invalid_arguments_get_message_from_entry(capsys):
    # Test invalid length message string
    raw_line = f'test, 0x1, 0'
    error_value = get_message_from_entry(raw_line, 0, Message())
    assert error_value is None or error_value == -1

    # Invalid characters like 'é' or '%'
    names_to_test = ['%test%', '°test°', 'étesté', '-test-']
    for name in names_to_test:
        check_message_report_error(capsys, name, 0x100)

    # Test message id not an int
    ids_to_test = [45.7, True]
    for message_id in ids_to_test:
        check_message_report_error(capsys, 'test', message_id)


def check_board_report_error(capsys, name, offset, extend, endianness):
    raw_line = f'{name}, {offset}, {extend}, {endianness}'
    error_value = get_board_from_entry(raw_line, 0, Board())
    out, err = capsys.readouterr()
    assert out != '' and error_value == -1, \
           f'get_board_from_entry() failed to print error with name = test, offset = {offset}, extend = {extend} ' \
           f'and endianness = {endianness}'


def test_invalid_arguments_get_board_from_entry(capsys):
    # Test invalid length board string
    raw_line = f'test, 0x1, 0, 0, 0'
    error_value = get_board_from_entry(raw_line, 0, Board())
    assert error_value is None or error_value == -1

    # Test error reporting with invalid characters
    names_to_test = ['%test%', '°test°', 'étesté', '-test-']
    for name in names_to_test:
        check_board_report_error(capsys, name, 0, 0, 0)

    # Check invalid offsets errors
    offsets_to_test = [45.7, True]
    for offset in offsets_to_test:
        check_board_report_error(capsys, 'test', {offset}, 0, 0)

    # Check invalid extend or endianness bool (0, 1) errors
    bools_to_test = [-1, 2]
    for value in bools_to_test:
        check_board_report_error(capsys, 'test', 0, {value}, 0)
        check_board_report_error(capsys, 'test', 0, 0, {value})

