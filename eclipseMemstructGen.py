import memparser
import sys
import os

from message_mod import Message
from signal_mod import Signal
from board_mod import Board
import memstructh
import memstructc
import telemetryMemstructh
import dbGen

with open("memstruct_entry.txt") as raw_entry:

	board_list = []
	first_board = 1
	first_mes = 1
	signal_cnt = 0

	# parse each entry
	for index, line in enumerate(raw_entry, start=1):
		code, sep, params = line.partition(':')
		params = params.upper()
		if code == 'b':
			# Board
			board = Board()
			memparser.get_board_from_entry(params, index, board)
			if board == -1:
				sys.exit()
			board_list.append(board)

		elif code == 'm':
			# Message
			mes = Message()
			memparser.get_message_from_entry(params, index, mes)
			if mes == -1:
				sys.exit()
			board.add_message(mes)

		elif code == 's':
			# Signal
			sig = Signal()
			memparser.get_signal_from_entry(params, index, signal_cnt, sig)
			if sig == -1:
				sys.exit()
			signal_cnt += 1
			mes.add_signal(sig)

		else:
			continue

	# Create output folder for generated files
	try:
		os.mkdir("output")
	except OSError:
		pass

	# Microcontroller CAN description files
	memstructh.generate(board_list)
	memstructc.generate(board_list)
	# CAN Vector Analyzer DB CAN description file
	dbGen.generate(board_list)
	# Telemetry backend CAN memstruct file
	telemetryMemstructh.generate(board_list)
