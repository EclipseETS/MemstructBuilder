import parser
import sys
import os
import pdb
from message_mod import message
from signal_mod import signal
from board_mod import boards
import memstructh
import memstructc
import xmlGen

raw_entry = open("memstruct_entry.txt")

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
		parser.get_board_from_entry(line, index, board)
		if(board == -1):
			sys.exit()
		board_list.append(board)

	elif(line.startswith("m:")): #message
		line = line.upper()
		line = line[2:]

		mes = message()
		parser.get_message_from_entry(line, index, mes)
		if(mes == -1):
			sys.exit()
		board.add_message(mes)

	elif(line.startswith("s:")): #signal
		line = line.upper()
		line = line[2:]
		sig = signal()
		parser.get_signal_from_entry(line, index, signal_cnt, sig)
		if(sig == -1):
			sys.exit()
		signal_cnt += 1
		mes.add_signal(sig)

	else:
		continue 


#Get Global Definition file(opt)

try:
	os.mkdir("output")
except:
	pass

memstructh.generate(board_list)
memstructc.generate(board_list)

xmlGen.generate(board_list)

#generate memstruct vector