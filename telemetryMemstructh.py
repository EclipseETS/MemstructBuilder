
import sys
import os
from message_mod import message
from signal_mod import signal
from board_mod import boards

def generate(board_list):
    try:
        os.remove("output/telemetry_memstruct.h")
    except:
        pass

    fo = open("output/telemetry_memstruct.h", "w+")
    
    #Start with header generation
    fo.write("/* This file was generate by EclipseMemstructGen.py*/\n")
    fo.write("#ifndef TELEMETRY_MEMSTRUCT_H_\n")
    fo.write("#define TELEMETRY_MEMSTRUCT_H_\n\n")

    # includes
    fo.write('#include <vector>\n')
    fo.write("#include <algorithm>\n")
    fo.write("#include <array>\n")
    fo.write("#include <string_view>\n")
    fo.write("using namespace std::literals::string_view_literals;\n\n")
    
    fo.write('#define CANFRM_EXTENDED_ID  (1<<29)\n')
    fo.write('#define CANFRM_RTR          (1<<30)\n\n')

    fo.write("#define MAX_SIG_CNT 8\n\n")

    fo.write("#define L_ENDIAN 0\n")
    fo.write("#define B_ENDIAN 1\n\n")

    # Type descriptions
    fo.write("enum DATA_TYPE\n")
    fo.write("{\n")
    fo.write("        TYPE_FLOATING = 0x10,\n")
    fo.write("                TYPE_float,\n")
    fo.write("                TYPE_double,\n")
    fo.write("        TYPE_UNSIGNED = 0x20,\n")
    fo.write("                TYPE_uint32_t,\n")
    fo.write("                TYPE_uint16_t,\n")
    fo.write("                TYPE_uint8_t,\n")
    fo.write("        TYPE_SIGNED = 0x40,\n")
    fo.write("                TYPE_int32_t,\n")
    fo.write("                TYPE_int16_t,\n")
    fo.write("                TYPE_int8_t\n")
    fo.write("};\n\n")
    
    # Generate Board Enum
    fo.write("/*Board enum*/\n")
    fo.write("enum{\n")
    for board in board_list:
        board.print_enum(fo)
    fo.write("};\n\n")

    # Generate Message List
    fo.write("/*Message enum*/\n")
    fo.write("enum CAN_ID\n")
    fo.write("{\n")
    for board in board_list:
        board.print_header(fo)
        board.print_message_enum_telemetry(fo)
    fo.write("};\n\n")

    # Generate Signal List
    fo.write("/*Signal enum*/\n")
    fo.write("enum SIGNAL_ID\n")
    fo.write("{\n")
    for board in board_list:
        board.print_header(fo)
        board.print_signal_enum(fo)
    fo.write("\n")
    fo.write("NUM_SIGNAL_IDS,")
    fo.write("};\n\n")

    # Print defintion of Signal decode struct
    fo.write(" /*  SignalDecode struct  */\n")
    fo.write("struct SignalDecode\n")
    fo.write("{\n")
    fo.write("        uint32_t id;\n")
    fo.write("        std::string_view name;\n")
    fo.write("        DATA_TYPE type;\n")
    fo.write("        uint32_t byte_pos;\n")
    fo.write("        uint32_t size;\n")
    fo.write("        uint8_t endianness;\n")
    fo.write("};\n\n")
    
    # Print defintion of CAN message decode struct
    fo.write(" /*  MessageDecode struct  */\n")
    fo.write("struct MessageDecode\n")
    fo.write("{\n")
    fo.write("        uint32_t id;\n")
    fo.write("        uint32_t pos;\n")
    fo.write("        std::string_view name;\n")
    fo.write("        uint32_t num_signals;\n")
    fo.write("        SignalDecode signals[MAX_SIG_CNT];  /* Signals */\n")
    
    fo.write("};\n\n")

    #print mesage definition
    num_can_messages = 0
    for board in board_list:
        num_can_messages = num_can_messages + board.message_cnt
    fo.write("static constexpr std::array<std::pair<uint32_t, MessageDecode>, {}> CAN_MESSAGES \n".format(num_can_messages))
    fo.write("{{\n")

    for board in board_list:
        board.print_header(fo)
        board.print_message_def_telemetry(fo)
    fo.write("}};\n\n")
    
    # End header guard and close file
    fo.write("#endif\n")
    fo.close()
