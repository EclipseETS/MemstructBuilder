
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

    assert message.signal_cnt == 2
    assert message.signal[0] == signal1
    assert message.signal[1] == signal2


def test_print_callback():
    message = Message()
    message.add_signal(Signal())
    message.add_signal(Signal())
    # Test that last character is not '\n'
    assert message.print_callback()[-1] != '\n'


def test_print_signal_enum():
    message = Message()
    message.add_signal(Signal())
    message.add_signal(Signal())
    # Test that last character is not '\n'
    assert message.print_signal_enum()[-1] != '\n'


def test_print_enum():
    message = Message()
    message.name = "test_name"
    message.id = 100

    # Test with last_id == id - 1, (message follows)
    test_string_next = f"        test_name,\n"
    # Test with last_id not previous (message does not follow)
    test_string_not_next = f"        test_name = 100,\n"

    # Id 99 is previous message
    assert message.print_enum(99) == test_string_next
    # Id 98 is not previous message
    assert message.print_enum(98) == test_string_not_next


def test_print_enum_full_id():
    board = Board()
    board.name = "test_board"
    message = Message()
    message.id = 42
    message.name = "test_message"
    board.add_message(message)

    test_string_next = f"        test_message"
    test_string_id_zero = f"        test_message = ID_OFFSET_test_board"
    test_string_not_next = f"        test_message = 42+ID_OFFSET_test_board"

    # Test message follows last message (not explicit index in string)
    assert message.print_enum_full_id(41, board) == test_string_next
    # Test message does not follow, but is 0
    message.id = 0
    assert message.print_enum_full_id(56, board) == test_string_id_zero
    # Test message does not follow nor is zero
    message.id = 42
    assert message.print_enum_full_id(4, board) == test_string_not_next


def create_test_message(num_signals):
    message = Message()
    message.name = 'message_test'
    for i in range(num_signals):
        signal = Signal()
        signal.name = f'signal{i}'
        signal.type = 'U32'
        signal.id = i + 0x200
        signal.init_value = 0
        message.add_signal(signal)

    return message


def test_print_para_macro():
    message = create_test_message(5)

    # Make sure last character is not '\n'
    assert message.print_para_macro(True)[-1] != '\n'
    assert message.print_para_macro(False)[-1] != '\n'


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

    message.add_signal(signal1)
    message.add_signal(signal2)

    little_endian_to_test = [True, False]  # [LITTLE, BIG]
    values_to_test = itertools.product(little_endian_to_test)

    # Testing that the addon 'CANFRM_LITTLE_ENDIAN' is added only if message is little_endian
    # Testing byte_pos calculation is correct (U8 + U32)
    for little_endian in values_to_test:
        byte_pos = 0  # Byte pos for first signal
        byte_pos_string = f'({byte_pos})|(CANFRM_LITTLE_ENDIAN)' if little_endian else f'{byte_pos}'
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
        byte_pos = f'0 + sizeof(U32)'  # Byte pos for second signal
        byte_pos_string = f'({byte_pos})|(CANFRM_LITTLE_ENDIAN)' if little_endian else f'{byte_pos}'
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

    message.add_signal(signal1)
    message.add_signal(signal2)

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


