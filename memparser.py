import re
from signal_mod import signal
from board_mod import boards
from message_mod import message

def get_signal_from_entry(raw_entry, line, signal_no, sig):

	raw_entry = raw_entry.replace("\t", "")
	raw_entry = raw_entry.replace("\n", "")
	raw_entry = raw_entry.replace(" ", "")

	entry = raw_entry.split(",")

	if(len(entry) != 8):
		print "Not enough or to much parameters at line: {}".format(line)
		return -1

	signal_name = entry[0]
	if(re.match("[^A-Za-z0-9_ ]", signal_name)):
		print "Bad Signal name at line: {}".format(line)
		return -1

	datatype = entry[1]
	if(entry[1] == "F"):
		datatype = "float"
		bitsize = 32
		isfloat = "true"
		issigned = "true"
	elif(entry[1] == "U16"):
		datatype = "uint16_t"
		bitsize = 16
		isfloat = "false"
		issigned = "false"
	elif(entry[1] == "U8"):
		datatype = "uint8_t"
		bitsize = 8
		isfloat = "false"
		issigned = "false"
	elif(entry[1] == "U32"):
		datatype = "uint32_t"
		bitsize = 32
		isfloat = "false"
		issigned = "false"
	elif(entry[1] == "8"):
		datatype = "int8_t"
		bitsize = 8
		isfloat = "false"
		issigned = "true"
	elif(entry[1] == "16"):
		datatype = "int16_t"
		bitsize = 16
		isfloat = "false"
		issigned = "true"
	elif(entry[1] == "32"):
		datatype = "int32_t"
		bitsize = 32
		isfloat = "false"
		issigned = "true"
	else:
		print "Bad datatype at line: {}".format(line)
		return -1

	try:
		init_value = int(entry[2])
	except:
		print "Init value is not a valid number at line : {}".format(line)
		return -1

	try:
		factor = int(entry[3])
	except:
		try:
			factor = float(entry[3])
		except:
			print "Factor is not a valid number"

	try:
		offset = int(entry[4])
	except:
		print "Offset value is not a valid number at line : {}".format(line)
		return -1

	unit_name = entry[5]
	if(re.match("[^A-Za-z]", unit_name)):
		print "Bad unit name at line: {}".format(line)
		return -1

	try:
		minvalue = int(entry[6])
	except:
		try:
			minvalue = float(entry[6])
		except:
			print "minvalue value is not a valid number at line : {}".format(line)

        

	try:
		maxvalue = int(entry[7])
	except:
		try:
			maxvalue = float(entry[7])
		except:
			print "maxvalue value is not a valid number at line : {}".format(line)

	sig.set_params(signal_name, signal_no, datatype, init_value, factor, offset, unit_name, minvalue, maxvalue, bitsize, issigned, isfloat)

	return sig

def get_board_from_entry(board_entry, line, board):

	board_entry = board_entry.replace("\t", "")
	board_entry = board_entry.replace("\n", "")
	board_entry = board_entry.replace("\r", "")
	board_entry = board_entry.replace(" ", "")

	entry = board_entry.split(",")

	if (len(entry) != 4):
		print "Not enough parameters at line: {}".format(line)
		return

	board_name = entry[0]
	if(re.match("[^A-Za-z0-9_ ]", board_name)):
		print "Bad board name at line: {}".format(line)
		return -1

	try:
		offset = int(entry[1], 16)
	except:
		print "Board offset is not a valid number"
		return -1

	if(entry[2] == "1"):
		extend = 1
	elif(entry[2] == "0"):
		extend = 0
	else:
		print "adress_extend value is not a valid number at line : {}".format(line)
		print entry[2]
		return -1


	if(entry[3] == "1"):
		little_endian = 1
	elif(entry[3] == "0"):
		little_endian = 0
	else:
		print "is_little_endian value is not a valid number at line : {}".format(line)
		return -1

	board.set_params(board_name, offset, extend, little_endian)

	return board


def get_message_from_entry(message_entry, line, mes):

	message_entry = message_entry.replace("\t", "")
	message_entry = message_entry.replace("\n", "")
	message_entry = message_entry.replace(" ", "")

	entry = message_entry.split(",")

	if (len(entry) != 2):
		print "Not enough parameters at line: {}".format(line)
		return

	message_name = entry[0]
	if(re.match("[^A-Za-z0-9_ ]", message_name)):
		print "Bad Signal name at line: {}".format(line)
		return -1

	try:
		message_id = int(entry[1], 16)
	except:
		print "Message ID is not a number at line: {}".format(line)
		return -1

	mes.set_params(message_name, message_id)

	return mes
