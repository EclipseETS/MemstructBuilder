
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

    assert board.message_cnt == 1
    assert board.message[board.message_cnt-1] == message


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


def test_print_callback():
    num_messages = 5
    num_signals = 2
    board = create_board_with_messages(num_messages, num_signals)

    # Making sure all signals have callbacks (5*2) and last callback
    # does not have a newline character
    test_string = ''
    for i in range(num_messages - 1):
        test_string += f'{board.message[i].print_callback()}\n'
    test_string += f'{board.message[num_messages - 1].print_callback()}'

    assert board.print_callback() == test_string


def test_print_enum():
    board1 = Board()
    board1.name = "Board_1"
    board1.offset = 0x200
    board1.extend = False
    board2 = Board()
    board2.name = "Board_2"
    board2.offset = 0x500
    board2.extend = True

    # Test that no newline character is returned and id is hexadecimal in format '0xAB'
    # Without extended id qualifier (CANFRM_EXTENDED_ID)
    test_string1 = "        ID_OFFSET_{} = {:#02x}".format(board1.name, board1.offset)
    # With extended id qualifier (CANFRM_EXTENDED_ID)
    test_string2 = "        ID_OFFSET_{} = {:#02x}L | CANFRM_EXTENDED_ID".format(board2.name, board2.offset)

    assert board1.print_enum() == test_string1
    assert board2.print_enum() == test_string2


def test_print_signal_enum():
    # Board with 5 messages with 2 signals each
    board = create_board_with_messages(5, 2)

    # Test that enum is spaced with ',\n' except last line
    test_string = ''
    for i in range(board.message_cnt - 1):
        test_string += f'{board.message[i].print_signal_enum()},\n'
    test_string += f'{board.message[board.message_cnt - 1].print_signal_enum()}'

    assert board.print_signal_enum() == test_string


def test_print_message_enum():
    # Board with 5 messages with 2 signals each
    board = create_board_with_messages(5, 2)
    board.message[0].id = 30
    board.message[1].id = 34
    board.message[2].id = 35
    board.message[3].id = 36
    board.message[4].id = 45

    # Test that all messages are present in enum
    test_string = ""
    last_id = -100
    for i in range(board.message_cnt):
        test_string += f'{board.message[i].print_enum(last_id)}'
        last_id = board.message[i].id
    test_string += f"        M_MAX_{board.name} = {board.message_cnt}"

    assert board.print_message_enum() == test_string


def test_print_message_enum_telemetry():
    board = create_board_with_messages(5, 2)
    # Test that last character is not '\n'
    assert board.print_message_enum_telemetry()[-1] != '\n'


def test_print_para_macro():
    board = create_board_with_messages(5, 2)
    # Test that last character is not '\n'
    assert board.print_para_macro(False)[-1] != '\n'
    assert board.print_para_macro(True)[-1] != '\n'


def test_print_txrx():
    board = Board()
    board.name = "test_name"

    test_string = (
        f"#ifndef M_test_name_TXRX\n"
        f"#        define M_test_name_TXRX CANMSG_RX\n"
        f"#endif\n"
    )

    assert board.print_txrx() == test_string


def test_print_message_def():
    board = create_board_with_messages(5, 2)
    # Test that last characters is not '\n'
    assert board.print_message_def()[-1] != '\n'


def test_print_message_def_telemetry():
    board = create_board_with_messages(5, 2)
    # Test that last characters is not '\n'
    assert board.print_message_def_telemetry()[-1] != '\n'

