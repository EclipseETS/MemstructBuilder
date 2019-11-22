import sys
from message_mod import message
from signal_mod import signal
from board_mod import boards

def generate(board_list):

	try:
		os.remove("output/memstruct.c")
	except:
		pass

	fo = open("output/memstruct.c", "w+")

	#Start with header generation
	fo.write("/* This file was generate by EclipseMemstructGen.py*/\n")
	fo.write("#ifndef E92_EXCLUDE_MAIN_MEMSTRUCT\n\n")

	fo.write('#include <stdint.h>\n\n')
	fo.write('#include "can_sig.h"\n')
	fo.write('#include "can_msg.h"\n\n')
	fo.write('#include "memstruct.h"\n\n')
	
	fo.write("#ifdef E92_USE_CUSTOM_MEMSTRUCT\n")
	fo.write('    #include "custom_memstruct.h"\n')
	fo.write("#endif\n\n")

	fo.write("#define CAN_PARA_MACRO(signame, width, initValue, callback) { CANSIG_UNCHANGED, width, initValue, callback }\n\n")
	fo.write("CANSIG_DATA CanSigTbl[CANSIG_N];\n")
	fo.write("const CANSIG_PARA CanSig[CANSIG_N] = {\n")

	#print CAN_PAR_MACRO
	board_cnt = len(board_list)
	for index, board in enumerate(board_list, start = 1):
		board.print_header(fo)
		if index == board_cnt:
			board.print_para_macro(fo, 1)
		else:
			board.print_para_macro(fo, 0)
	fo.write("};\n\n")

	#print TXRX define
	for board in board_list:
		board.print_txrx(fo)
	fo.write("\n\n")

	#print mesage definition
	fo.write("const CANMSG_PARA CanMsg[CANMSG_N] = {\n")

	for board in board_list:
		board.print_header(fo)
		board.print_message_def(fo)

	fo.write("#ifdef E92_USE_CUSTOM_MEMSTRUCT\n")
	fo.write("/*******************************************************************/\n")
	fo.write("/*                                                    CUSTOM CAN                                                         */\n")
	fo.write("/********************************************************************/\n")
	fo.write("        CUSTOM_CAN_MSG,\n")
	fo.write("#endif\n")
	fo.write("        /*******************************************************************/\n")
	fo.write("        /*                                                        Last Item                                                                        */\n")
	fo.write("        /********************************************************************/\n")
	fo.write("        {\n")
	fo.write("                0, /* CAN-Identifier */\n")
	fo.write("                0, /* Message Type */\n")
	fo.write("                0, /* DLC of Message */\n")
	fo.write("                0, /* No. of Links */\n")
	fo.write("        },\n")
	fo.write("};\n\n")
	
	fo.write("#endif /*EXCLUDE_MAIN_MEMSTRUCT*/")



	fo.close()
