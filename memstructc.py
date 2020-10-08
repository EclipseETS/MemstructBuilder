import sys
import os
from message_mod import message
from signal_mod import signal
from board_mod import boards

def generate(board_list):

	if os.path.exists("output/memstruct.c"):
		try:
			os.remove("output/memstruct.c")
		except:
			print("ERROR: Failed to delete memstruct.c in output")
			sys.exit()
	
	with open("output/memstruct.c", "w+") as fo:
		
		# Start with headers, includes and defines generation
		str = (
			f"/* This file was generated by EclipseMemstructGen.py*/\n"
			f"\n"
			f"#ifndef E92_EXCLUDE_MAIN_MEMSTRUCT\n"
			f"\n"
			f"#include <stdint.h>\n"
			f"\n"
			f"#include \"can_sig.h\"\n"
			f"#include \"can_msg.h\"\n"
			f"\n"
			f"#include \"memstruct.h\"\n"
			f"\n"
			f"#ifdef E92_USE_CUSTOM_MEMSTRUCT\n"
			f"    #include \"custom_memstruct.h\"\n"
			f"#endif\n"
			f"\n"
			f"#define CAN_PARA_MACRO(signame, width, initValue, callback) {{ CANSIG_UNCHANGED, width, initValue, callback }}\n"
			f"\n"
			f"CANSIG_DATA CanSigTbl[CANSIG_N];\n"
		)

		# Generate CAN_PAR_MACRO
		can_par_macro_str = ""
		board_cnt = len(board_list)
		for index, board in enumerate(board_list, start = 1):
			can_par_macro_str += board.print_header()
			if index == board_cnt:
				can_par_macro_str += board.print_para_macro(1)
			else:
				can_par_macro_str += board.print_para_macro(0)
		str += (
			f"const CANSIG_PARA CanSig[CANSIG_N] = {{\n"
			f"{can_par_macro_str}"
			f"}};\n"
			f"\n"
		)

		# Generate TXRX define
		for board in board_list:
			str += board.print_txrx()
		str += f"\n\n"

		# Generate mesage definition
		message_def_str = ""
		for board in board_list:
			message_def_str += board.print_header()
			message_def_str += board.print_message_def()
		str += (
			f"const CANMSG_PARA CanMsg[CANMSG_N] = {{\n"
			f"{message_def_str}"
			f"#ifdef E92_USE_CUSTOM_MEMSTRUCT\n"
			f"/*******************************************************************/\n"
			f"/*                                                    CUSTOM CAN                                                         */\n"
			f"/********************************************************************/\n"
			f"        CUSTOM_CAN_MSG,\n"
			f"#endif\n"
			f"        /*******************************************************************/\n"
			f"        /*                                                        Last Item                                                                        */\n"
			f"        /********************************************************************/\n"
			f"        {{\n"
			f"                0, /* CAN-Identifier */\n"
			f"                0, /* Message Type */\n"
			f"                0, /* DLC of Message */\n"
			f"                0, /* No. of Links */\n"
			f"        }},\n"
			f"}};\n"
			f"\n"
			f"#endif /*EXCLUDE_MAIN_MEMSTRUCT*/\n"
		)
		
		# Writing into file
		fo.write(str)
