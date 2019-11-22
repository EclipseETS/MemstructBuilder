import sys
import os
from message_mod import message
from signal_mod import signal
from board_mod import boards

def generate(board_list):

	try:
		os.remove("output/memstruct.h")
	except:
		pass

	fo = open("output/memstruct.h", "w+")

	#Start with header generation
	fo.write("/* This file was generate by EclipseMemstructGen.py*/\n")
	fo.write("#ifndef MEMSTRUCT_H_\n")
	fo.write("#define MEMSTRUCT_H_\n\n")
	fo.write("#ifndef E92_EXCLUDE_MAIN_MEMSTRUCT\n\n")
	fo.write('#include <stddef.h>\n\n')
	fo.write('#include "can_cfg.h"\n')
	fo.write('#include "can_sig.h"\n')
	fo.write('#include "can_msg.h"\n')
	fo.write('#include "can_frm.h"\n\n')
	fo.write("#ifdef E92_USE_CUSTOM_MEMSTRUCT\n")
	fo.write('       #include "custom_memstruct.h"\n')
	fo.write("#endif\n")
	fo.write('#include "service_can_callbacks.h"\n\n')
	fo.write('#define CANFRM_EXTENDED_ID  (1<<29)\n')
	fo.write('#define CANFRM_RTR          (1<<30)\n\n')

	#TODO Add global define here from an input file

	#Generate Callback
	fo.write("/*Callback definition*/\n")
	for board in board_list:
		board.print_header(fo)
		board.print_callback(fo)

	#Generate Board enum
	fo.write("/*Board enum*/\n")
	fo.write("enum{\n")
	for board in board_list:
		board.print_enum(fo)
	fo.write("};\n")

	#Generate Signal List
	fo.write("/*Signal enum*/\n")
	fo.write("enum{\n")
	for board in board_list:
		board.print_header(fo)
		board.print_signal_enum(fo)
	fo.write("\n#ifdef E92_USE_CUSTOM_MEMSTRUCT\n")
	fo.write("        S_CUSTOM_SIGNALS_ID\n")
	fo.write("#endif\n")
	fo.write("};\n")

	#Generate Message List
	fo.write("/*Message enum*/\n")
	fo.write("enum{\n")
	for board in board_list:
		board.print_header(fo)
		board.print_message_enum(fo)
	fo.write("};\n\n")

	#print Define M_max
	cnt = 0
	for board in board_list:
		cnt += board.message_cnt

	fo.write("#define M_MAX                 {}\n\n".format(cnt))
	fo.write("#endif /*E92_EXCLUDE_MAIN_MEMSTRUCT*/\n")
	fo.write("#endif\n")
	fo.close()



