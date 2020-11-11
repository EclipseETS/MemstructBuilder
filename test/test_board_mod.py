
import itertools
from board_mod import Board
from message_mod import Message
from signal_mod import Signal


def test_set_params():
    test_name = "test_name"
    test_offset = 0x200
    test_extend = 0x100
    test_little_endian = True

    board = Board()
    board.set_params(test_name, test_offset, test_extend, test_little_endian)

    assert board.name == test_name
    assert board.offset == test_offset
    assert board.extend == test_extend
    assert board.little_endian == test_little_endian


def test_add_message():
    board = Board()
    message = Message()

    board.add_message(message)

    assert len(board.messages) == 1
    assert board.messages[0] == message


def test_print_header():
    board = Board()
    test_string = '/' + '*' * board.header_width + '/\n'
    test_string += f'/*{board.name: ^{board.header_width - 2}}*/\n'
    test_string += '/' + '*' * board.header_width + '/\n'
    assert board.print_header() == test_string


def create_message_with_signals(num_signals):
    message = Message()
    for i in range(num_signals):
        signal = Signal()
        signal.name = f'Signal{i}'
        message.add_signal(signal)
    return message


def create_board_with_messages(num_messages, num_signals):
    board = Board()
    for i in range(num_messages):
        message = create_message_with_signals(num_signals)
        message.name = f'Message{i}'
        board.add_message(message)
    return board


def test_print_callback_should_not_end_with_newline_character():
    num_messages = 5
    num_signals = 2
    board = create_board_with_messages(num_messages, num_signals)

    test_string = ''
    for i in range(num_messages - 1):
        test_string += f'{board.messages[i].print_callback()}\n'
    test_string += f'{board.messages[-1].print_callback()}'

    assert board.print_callback() == test_string


def test_print_enum_with_extend_false():
    board = Board()
    board.name = "Board_1"
    board.offset = 0x200
    board.extend = False

    # Without extended id qualifier (CANFRM_EXTENDED_ID)
    test_string = "        ID_OFFSET_{} = {:#02x}".format(board.name, board.offset)

    assert board.print_enum() == test_string


def test_print_enum_with_extend_true():
    board = Board()
    board.name = "Board_2"
    board.offset = 0x500
    board.extend = True

    # With extended id qualifier (CANFRM_EXTENDED_ID)
    test_string = "        ID_OFFSET_{} = {:#02x}L | CANFRM_EXTENDED_ID".format(board.name, board.offset)

    assert board.print_enum() == test_string


def test_print_signal_enum_should_not_end_with_newline_character():
    board = create_board_with_messages(num_messages=5, num_signals=2)

    # Test that enum is spaced with ',\n' except last line
    test_string = ''
    for i in range(len(board.messages) - 1):
        test_string += f'{board.messages[i].print_signal_enum()},\n'
    test_string += f'{board.messages[-1].print_signal_enum()}'

    assert board.print_signal_enum() == test_string


def test_print_message_enum():
    board = create_board_with_messages(num_messages=5, num_signals=2)
    board.messages[0].id = 30
    board.messages[1].id = 34
    board.messages[2].id = 35
    board.messages[3].id = 36
    board.messages[4].id = 45

    # Test that all messages are present in enum
    test_string = ""
    last_id = -100
    for i in range(len(board.messages)):
        test_string += f'{board.messages[i].print_enum(last_id)}'
        last_id = board.messages[i].id
    test_string += f"        M_MAX_{board.name} = {len(board.messages)}"

    assert board.print_message_enum() == test_string


def test_print_message_enum_telemetry_should_not_end_with_newline_character():
    board = create_board_with_messages(num_messages=5, num_signals=2)
    assert not board.print_message_enum_telemetry().endswith('\n')


def test_print_para_macro_not_last_should_not_end_with_newline_character():
    board = create_board_with_messages(num_messages=5, num_signals=2)
    assert not board.print_para_macro(False).endswith('\n')


def test_print_para_macro_is_last_should_not_end_with_newline_character():
    board = create_board_with_messages(num_messages=5, num_signals=2)
    assert not board.print_para_macro(True).endswith('\n')


def test_print_txrx():
    board = Board()
    board.name = "test_name"

    test_string = (
        f"#ifndef M_test_name_TXRX\n"
        f"#        define M_test_name_TXRX CANMSG_RX\n"
        f"#endif\n"
    )

    assert board.print_txrx() == test_string


def test_print_message_def_should_not_end_with_newline_character():
    board = create_board_with_messages(num_messages=5, num_signals=2)
    assert not board.print_message_def().endswith('\n')


def test_print_message_def_telemetry_should_not_end_with_newline_character():
    board = create_board_with_messages(num_messages=5, num_signals=2)
    assert not board.print_message_def_telemetry().endswith('\n')

