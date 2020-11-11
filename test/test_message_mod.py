
import itertools
from board_mod import Board
from message_mod import Message
from signal_mod import Signal


def test_set_params():
    test_name = "test_name"
    test_id = 20

    message = Message()
    message.set_params(test_name, test_id)

    assert message.name == test_name
    assert message.id == test_id


def test_add_signal():
    message = Message()
    signal1 = Signal()
    signal2 = Signal()

    message.add_signal(signal1)
    message.add_signal(signal2)

    assert len(message.signals) == 2
    assert message.signals[0] == signal1
    assert message.signals[1] == signal2


def test_print_callback_should_not_end_with_newline_character():
    message = Message()
    message.signals.append(Signal())
    message.signals.append(Signal())
    assert not message.print_callback().endswith('\n')


def test_print_signal_enum_should_not_end_with_newline_character():
    message = Message()
    message.signals.append(Signal())
    message.signals.append(Signal())
    assert not message.print_signal_enum().endswith('\n')


def test_print_enum_with_message_id_is_not_following_last_message():
    message = Message()
    message.name = "test_name"
    message.id = 100
    test_string_not_next = f"        test_name = 100,\n"

    # Id 98 is not previous message
    assert message.print_enum(98) == test_string_not_next


def test_print_enum_with_message_id_is_following_last_message():
    message = Message()
    message.name = "test_name"
    message.id = 100
    test_string_next = f"        test_name,\n"

    # Id 99 is previous message
    assert message.print_enum(99) == test_string_next


def create_board_with_message(message_id):
    board = Board()
    board.name = "test_board"
    message = Message()
    message.id = message_id
    message.name = "test_message"
    board.messages.append(message)
    return message, board


def test_print_enum_full_id_with_message_is_following_last_message():
    message, board = create_board_with_message(message_id=42)
    test_string_next = f"        test_message"
    assert message.print_enum_full_id(last_id=41, board=board) == test_string_next


def test_print_enum_full_id_with_message_not_following_last_but_has_id_zero():
    message, board = create_board_with_message(message_id=0)
    test_string_id_zero = f"        test_message = ID_OFFSET_test_board"
    # Test message does not follow, but is 0
    assert message.print_enum_full_id(last_id=56, board=board) == test_string_id_zero


def test_print_enum_full_id_with_message_not_following_last_message_and_id_not_zero():
    message, board = create_board_with_message(message_id=42)
    test_string_not_next = f"        test_message = 42+ID_OFFSET_test_board"
    assert message.print_enum_full_id(last_id=4, board=board) == test_string_not_next


def create_test_message(num_signals):
    message = Message()
    message.name = 'message_test'
    for i in range(num_signals):
        signal = Signal()
        signal.name = f'signal{i}'
        signal.type = 'U32'
        signal.id = i + 0x200
        signal.init_value = 0
        message.signals.append(signal)

    return message


def test_print_para_macro_with_last_true_should_not_end_with_newline_character():
    message = create_test_message(5)
    assert not message.print_para_macro(True).endswith('\n')


def test_print_para_macro_with_last_false_should_not_end_with_newline_character():
    message = create_test_message(5)
    assert not message.print_para_macro(False).endswith('\n')


def test_print_message_def():
    board_name = "board_test"
    message = Message()
    message.name = "message_test"

    # Test signals
    signal1 = Signal()
    signal1.name = "signal1"
    signal1.type = "U32"
    signal2 = Signal()
    signal2.name = "signal2"
    signal2.type = "U8"

    message.signals.append(signal1)
    message.signals.append(signal2)

    little_endian_to_test = [True, False]  # [LITTLE, BIG]
    values_to_test = itertools.product(little_endian_to_test)

    # Testing that the addon 'CANFRM_LITTLE_ENDIAN' is added only if message is little_endian
    # Testing byte_pos calculation is correct (U8 + U32)
    for little_endian in values_to_test:
        test_string = (
            f"        {{\n"
            f"                ID_OFFSET_board_test + message_test, /* CAN-Identifier */\n"
            f"                M_board_test_TXRX, /* Message Type */\n"
            f"                sizeof(U32) + sizeof(U8), /* DLC of Message */\n"
            f"                2, /* No. of Links */\n"
            f"                {{\n"
            f"                        {{\n"
            f"                                signal1,       /* Signal ID */\n"
            f"                                (0)|(CANFRM_LITTLE_ENDIAN)  /* Byte Position */\n"
            f"                        }},\n"
        )
        test_string += (
            f"                        {{\n"
            f"                                signal2,       /* Signal ID */\n"
            f"                                (0 + sizeof(U32))|(CANFRM_LITTLE_ENDIAN)  /* Byte Position */\n"
            f"                        }}\n"  # No comma for last signal
        )
        test_string += (
            f"                }}\n"
            f"        }}"
        )

        assert message.print_message_def(board_name, little_endian) == test_string, \
               f'print_message_def() test failed with little endian = {little_endian}'


def test_print_message_def_telemetry():
    board_name = "board_test"
    message = Message()
    message.name = "message_test"

    # Test signals
    signal1 = Signal()
    signal1.name = "signal1"
    signal1.type = "U32"
    signal2 = Signal()
    signal2.name = "signal2"
    signal2.type = "U8"

    message.signals.append(signal1)
    message.signals.append(signal2)

    little_endian_to_test = [True, False]  # [LITTLE, BIG]
    values_to_test = itertools.product(little_endian_to_test)

    for little_endian in values_to_test:
        little_endian_string = f'L_ENDIAN' if little_endian else f'BIG_ENDIAN'
        factor_string_signal1 = f'{signal1.factor}.0f' if isinstance(signal1.factor, int) else f'{signal1.factor}f'
        factor_string_signal2 = f'{signal2.factor}.0f' if isinstance(signal2.factor, int) else f'{signal2.factor}f'
        test_string = (
            f"        {{\n"
            f"                message_test, /* CAN-Identifier */\n"
            f"                {{\n"
            f"                        message_test, /* CAN-Identifier */\n"
            f"                        sizeof(U32) + sizeof(U8), /* DLC of Message */\n"
            f'                        "message_test", /* Name of Message */\n'
            f"                        2, /* No. of Links */\n"
            f"                        {{\n"
            f"                                {{\n"
            f"                                        signal1,   /* Signal ID */\n"
            f'                                        "signal1",   /* Signal Name */\n'
            f"                                        TYPE_U32,   /* Signal Type */\n"
            f"                                        0,   /* Byte Position */\n"
            f"                                        sizeof(U32),   /* sizeof */\n"
            f"                                        {little_endian_string},   /* Endianness */\n"
            f"                                        {factor_string_signal1},   /* Multiplier */\n"
            f"                                }},\n"
            f"                                {{\n"
            f"                                        signal2,   /* Signal ID */\n"
            f'                                        "signal2",   /* Signal Name */\n'
            f"                                        TYPE_U8,   /* Signal Type */\n"
            f"                                        0 + sizeof(U32),   /* Byte Position */\n"
            f"                                        sizeof(U8),   /* sizeof */\n"
            f"                                        {little_endian_string},   /* Endianness */\n"
            f"                                        {factor_string_signal2},   /* Multiplier */\n"
            f"                                }}\n"
            f"                        }}\n"
            f"                }}\n"
            f"        }}"
        )

        assert message.print_message_def_telemetry(little_endian) == test_string, \
               f"print_message_def_telemetry() test failed with values: little_endian = {little_endian}"


