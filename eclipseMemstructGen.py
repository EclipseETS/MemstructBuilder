import memparser
import sys
import os
import pdb
from message_mod import message
from signal_mod import signal
from board_mod import boards
import memstructh
import memstructc
import telemetryMemstructh
import xmlGen
import dbGen

with open("memstruct_entry.txt") as raw_entry:

	board_list = []
	first_board = 1
	first_mes = 1
	signal_cnt = 0

	#parse each entry
	for index, line in enumerate(raw_entry, start = 1):
		if(line.startswith("b:")): #board
			line = line.upper()
			line = line[2:]

			board = boards()
			memparser.get_board_from_entry(line, index, board)
			if(board == -1):
				sys.exit()
			board_list.append(board)

		elif(line.startswith("m:")): #message
			line = line.upper()
			line = line[2:]

			mes = message()
			memparser.get_message_from_entry(line, index, mes)
			if(mes == -1):
				sys.exit()
			board.add_message(mes)

		elif(line.startswith("s:")): #signal
			line = line.upper()
			line = line[2:]
			sig = signal()
			memparser.get_signal_from_entry(line, index, signal_cnt, sig)
			if(sig == -1):
				sys.exit()
			signal_cnt += 1
			mes.add_signal(sig)

		else:
			continue

	# Create output folder for generated files
	if not os.path.exists("output"):
		try:
			os.mkdir("output")
		except:
			print("ERROR: Failed to create /output/ folder")
			sys.exit()

	# Microcontroller CAN description files
	memstructh.generate(board_list)
	memstructc.generate(board_list)
	# XML Generation
	xmlGen.generate(board_list)
	# CAN Vector Analyzer DB CAN description file
	dbGen.generate(board_list)
	# Telemetry backend CAN memstruct file
	telemetryMemstructh.generate(board_list)
