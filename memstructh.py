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
	fo.write('#include "preprocessor.h"\n')
	fo.write('#include "compiler.h"\n')
	fo.write('#include "can_cfg.h"\n')
	fo.write('#include "can_sig.h"\n')
	fo.write('#include "can_msg.h"\n')
	fo.write('#include "can_frm.h"\n')

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

	fo.write("#define M_MAX\t\t {}\n\n".format(cnt))
	fo.write("#endif\n")
	fo.close()



