
import itertools
from signal_mod import Signal


def test_set_params():
    # Test values
    test_name = 'test_name'
    test_id = 0x400
    test_datatype = 'U16'
    test_init_value = 42
    test_factor = 144
    test_offset = 8
    test_unit = 'RPM'
    test_minvalue = 0
    test_maxvalue = 65535
    test_bitsize = 16
    test_is_signed = False
    test_is_float = False

    signal = Signal()
    signal.set_params(test_name, test_id, test_datatype, test_init_value,
                      test_factor, test_offset, test_unit, test_minvalue, test_maxvalue,
                      test_bitsize, test_is_signed, test_is_float)

    assert signal.name == test_name
    assert signal.id == test_id
    assert signal.type == test_datatype
    assert signal.init_value == test_init_value
    assert signal.factor == test_factor
    assert signal.offset == test_offset
    assert signal.unit == test_unit
    assert signal.minvalue == test_minvalue
    assert signal.maxvalue == test_maxvalue
    assert signal.bitsize == test_bitsize
    assert signal.signed == test_is_signed
    assert signal.float == test_is_float


def test_print_callback():
    test_name = "name_test"
    test_string = (
        "#ifndef name_test_callback\n"
        "#        define name_test_callback NULL\n"
        "#endif"
    )

    signal = Signal()
    signal.name = test_name
    str_result = signal.print_callback()
    assert str_result == test_string


def test_print_enum():
    test_name = "name_test"
    test_string = "        name_test"

    signal = Signal()
    signal.name = test_name
    str_result = signal.print_enum()
    assert str_result == test_string


def test_print_para_macro():
    signal = Signal()
    signal.name = "test_name"

    for signal_type, init_value in {"U8": 255, "U16": 65000, "U32": 101, "F": 42.65}.items():
        signal.type = signal_type
        signal.init_value = init_value

        test_string = f"        CAN_PARA_MACRO(test_name, sizeof({signal_type}), " \
                      f"{init_value}, test_name_callback)"
        str_result = signal.print_para_macro(False)

        assert str_result == test_string, f"print_para_macro() test failed with inputs signal_type = {signal_type} " \
                                          f"and init value = {init_value}"


def test_last_print_para_macro():
    signal = Signal()
    signal.name = "test_name"

    for signal_type, init_value in {"U8": 255, "U16": 65000, "U32": 101, "F": 42.65}.items():
        signal.type = signal_type
        signal.init_value = init_value

        test_string = (
            f"        CAN_PARA_MACRO(test_name, sizeof({signal_type}), "
            f"{init_value}, test_name_callback),\n"
            f"\n"
            f"#ifdef E92_USE_CUSTOM_MEMSTRUCT\n"
            f"/*******************************************************************/\n"
            f"/*                           CUSTOM CAN                            */\n"
            f"/*******************************************************************/\n"
            f"        CUSTOM_CAN_SIG,\n"
            f"#endif"
        )
        str_result = signal.print_para_macro(True)

        assert str_result == test_string, f"print_para_macro() test failed with inputs signal_type = {signal_type} " \
                                          f"and init value = {init_value}"


def test_print_definition():
    signal = Signal()
    signal.name = "test_name"

    last_to_test = [False, True]
    little_endian_to_test = [True, False]  # [LITTLE, BIG]
    byte_pos_to_test = [8, 16]

    values_to_test = itertools.product(last_to_test, little_endian_to_test, byte_pos_to_test)

    for is_last, little_endian, byte_pos in values_to_test:
        comma_separator = '' if is_last else ','
        byte_pos_str = f"{byte_pos}" if not little_endian else \
                       f"({byte_pos})|(CANFRM_LITTLE_ENDIAN)"
        test_string = (
            f"                        {{\n"
            f"                                test_name,       /* Signal ID */\n"
            f"                                {byte_pos_str}  /* Byte Position */\n"
            f"                        }}{comma_separator}\n"
        )

        str_result = signal.print_definition(byte_pos, is_last, little_endian)
        assert str_result == test_string, f"print_definition() test failed with inputs is_last = {is_last} " \
                                          f", is_little_endian = {little_endian} and byte_pos = {byte_pos}"


def test_print_definition_telemetry():
    signal = Signal()
    signal.name = "test_name"

    last_to_test = [False, True]
    little_endian_to_test = [True, False]  # [LITTLE, BIG]
    byte_pos_to_test = [8, 16]
    factors_to_test = {'U8': 200, 'U16': 64555, 'U32': 42, 'F': 42.76}

    values_to_test = itertools.product(last_to_test, little_endian_to_test, byte_pos_to_test,
                                       factors_to_test.keys())

    for is_last, little_endian, byte_pos, signal_type in values_to_test:
        signal.type = signal_type
        signal.factor = factors_to_test[signal_type]

        comma_separator = '' if is_last else ','
        endianness = 'L_ENDIAN' if little_endian else 'B_ENDIAN'
        factor_str = f'{factors_to_test[signal_type]}.0f' if signal.type is not 'F' \
            else f'{factors_to_test[signal_type]}f'

        test_string = (
            f"                                {{\n"
            f"                                        test_name,   /* Signal ID */\n"
            f"                                        \"test_name\",   /* Signal Name */\n"
            f"                                        TYPE_{signal_type},   /* Signal Type */\n"
            f"                                        {byte_pos},   /* Byte Position */\n"
            f"                                        sizeof({signal_type}),   /* sizeof */\n"
            f"                                        {endianness},   /* Endianness */\n"
            f"                                        {factor_str},   /* Multiplier */\n"
            f"                                }}{comma_separator}\n"
        )

        str_result = signal.print_definition_telemetry(byte_pos, is_last, little_endian)
        assert str_result == test_string, f"print_definition_telemetry() test failed with inputs: is_last = {is_last}, " \
                                          f"is little endian = {little_endian}, byte_pos = {byte_pos}, " \
                                          f"signal type = {signal_type}, factor = {factors_to_test[signal_type]}"

