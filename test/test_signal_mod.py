
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

        last = False
        test_string_not_last = f"        CAN_PARA_MACRO(test_name, sizeof({signal_type}), " \
                               f"{init_value}, test_name_callback)"
        str_result_not_last = signal.print_para_macro(last)

        last = True
        test_string_last = (
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
        str_result_last = signal.print_para_macro(last)

        assert str_result_not_last == test_string_not_last
        assert str_result_last == test_string_last


def test_print_definition():
    signal = Signal()
    signal.name = "test_name"

    for last in [False, True]:
        for little_endian in [True, False]:  # [LITTLE, BIG]
            for byte_pos in [0, 8, 16, 24, 32, 40, 48, 56]:
                comma_separator = '' if last else ','
                byte_pos_str = f"{byte_pos}" if not little_endian else \
                               f"({byte_pos})|(CANFRM_LITTLE_ENDIAN)"
                test_string = (
                    f"                        {{\n"
                    f"                                test_name,       /* Signal ID */\n"
                    f"                                {byte_pos_str}  /* Byte Position */\n"
                    f"                        }}{comma_separator}\n"
                )

                str_result = signal.print_definition(byte_pos, last, little_endian)
                assert str_result == test_string


def test_print_definition_telemetry():
    signal = Signal()
    signal.name = "test_name"

    for last in [False, True]:
        for little_endian in [True, False]:  # [LITTLE, BIG]
            for byte_pos in [0, 8, 16, 24, 32, 40, 48, 56]:
                for signal_type, factor in {'U8': 200, 'U16': 64555, 'U32': 42, 'F': 42.76}.items():
                    signal.type = signal_type
                    signal.factor = factor

                    comma_separator = '' if last else ','
                    endianness = 'L_ENDIAN' if little_endian else 'B_ENDIAN'
                    factor_str = f'{factor}.0f' if signal_type is not 'F' else f'{factor}f'

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

                    str_result = signal.print_definition_telemetry(byte_pos, last, little_endian)
                    assert str_result == test_string

