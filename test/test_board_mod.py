
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

    board.messages.append(message)

    assert len(board.messages) == 1
    assert board.messages[0] == message


def create_message_with_signals(num_signals):
    message = Message()
    for i in range(num_signals):
        signal = Signal()
        signal.name = f'Signal{i}'
        message.signals.append(signal)
    return message


def create_board_with_messages(num_messages, num_signals):
    board = Board()
    for i in range(num_messages):
        message = create_message_with_signals(num_signals)
        message.name = f'Message{i}'
        board.messages.append(message)
    return board


def test_print_callback():
    board = create_board_with_messages(num_messages=5, num_signals=2)

    test_string = ''
    for i in range(len(board.messages)):
        for j in range(len(board.messages[i].signals)):
            # Last signal entry should not have newline character
            last_char = '\n' if not (i == len(board.messages) - 1 and j == len(board.messages[i].signals) - 1) else ''
            test_string += (
                f"#ifndef Signal{j}_callback\n"
                f"#        define Signal{j}_callback NULL\n"
                f"#endif{last_char}"
            )

    assert board.print_callback() == test_string


def test_print_enum_with_extend_false():
    board = Board()
    board.name = "Board_1"
    board.offset = 0x200
    board.extend = False

    # Without extended id qualifier (CANFRM_EXTENDED_ID)
    test_string = "        ID_OFFSET_Board_1 = 0x200"

    assert board.print_enum() == test_string


def test_print_enum_with_extend_true():
    board = Board()
    board.name = "Board_2"
    board.offset = 0x500
    board.extend = True

    # With extended id qualifier (CANFRM_EXTENDED_ID)
    test_string = "        ID_OFFSET_Board_2 = 0x500L | CANFRM_EXTENDED_ID"

    assert board.print_enum() == test_string


def test_print_signal():
    board = create_board_with_messages(num_messages=5, num_signals=2)

    # Test that enum is spaced with ',\n' except last line
    test_string = ''
    for i in range(len(board.messages)):
        for j in range(len(board.messages[i].signals)):
            # Last signal entry should not have newline character
            last_char = ',\n' if not (i == len(board.messages) - 1 and j == len(board.messages[i].signals) - 1) else ''
            test_string += f"        Signal{j}{last_char}"

    assert board.print_signal_enum() == test_string


def test_print_message_enum():
    board = create_board_with_messages(num_messages=5, num_signals=2)
    board.messages[0].id = 30
    board.messages[1].id = 34
    board.messages[2].id = 35
    board.messages[3].id = 36
    board.messages[4].id = 45

    # Test that all messages are present in enum with proper ids
    test_string = f"        Message0 = 30,\n"
    test_string += f"        Message1 = 34,\n"
    test_string += f"        Message2,\n"
    test_string += f"        Message3,\n"
    test_string += f"        Message4 = 45,\n"
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

