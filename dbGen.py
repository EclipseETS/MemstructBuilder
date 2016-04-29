import sys
import os
from message_mod import message
from signal_mod import signal
from board_mod import boards

def generate(board_list):

	try:
		os.remove("output/CAN_DB_E9.dbc")
	except:
		pass

	fo = open("output/CAN_DB_E9.dbc", "w+")

	fo.write('VERSION ""\n')
	fo.write('\n')
	fo.write('\n')
	fo.write('NS_ : \n')
	fo.write('\tNS_DESC_\n')
	fo.write('\tCM_\n')
	fo.write('\tBA_DEF_\n')
	fo.write('\tBA_\n')
	fo.write('\tVAL_\n')
	fo.write('\tCAT_DEF_\n')
	fo.write('\tCAT_\n')
	fo.write('\tFILTER\n')
	fo.write('\tBA_DEF_DEF_\n')
	fo.write('\tEV_DATA_\n')
	fo.write('\tENVVAR_DATA_\n')
	fo.write('\tSGTYPE_\n')
	fo.write('\tSGTYPE_VAL_\n')
	fo.write('\tBA_DEF_SGTYPE_\n')
	fo.write('\tBA_SGTYPE_\n')
	fo.write('\tSIG_TYPE_REF_\n')
	fo.write('\tVAL_TABLE_\n')
	fo.write('\tSIG_GROUP_\n')
	fo.write('\tSIG_VALTYPE_\n')
	fo.write('\tSIGTYPE_VALTYPE_\n')
	fo.write('\tBO_TX_BU_\n')
	fo.write('\tBA_DEF_REL_\n')
	fo.write('\tBA_REL_\n')
	fo.write('\tBA_DEF_DEF_REL_\n')
	fo.write('\tBU_SG_REL_\n')
	fo.write('\tBU_EV_REL_\n')
	fo.write('\tBU_BO_REL_\n')
	fo.write('\tSG_MUL_VAL_\n')
	fo.write('\n')
	fo.write('BS_:\n')
	fo.write('\n')
	fo.write('BU_:\n')
	fo.write('\n')
	fo.write('\n')

	float_footer = []
	for board in board_list:
		for message in board.message:
			dlc = 0

			# Signal offset
			if (board.little_endian == 1):
				signal_offset = 0
			else:
				signal_offset = 7

			# ID
			id = (board.offset + message.id)

			# Extended
			if (board.extend == 1):
				id = id | 0x80000000

			# DLC
			for signal in message.signal:
				dlc = dlc + (int(signal.bitsize) / 8)

			fo.write("BO_" + " " + str(id) + " " + str(message.name) + ": " + str(dlc) + " " + "Vector__XXX" + "\n")

			for signal in message.signal:
				# Signed
				if (signal.signed == "true"):
					signed = "-"
				else:
					signed = "+"
				# Endianess
				if (board.little_endian == 1):
					endianess = "1"
				else:
					endianess = "0"
				# Float footer
				if (signal.float == "true"):
					float_footer.append("SIG_VALTYPE_ " + str(id) + " " + str(signal.name) + " : 1;\n")

				fo.write(" SG_" + " " + str(signal.name) + " : " + str(signal_offset) + "|" + str(signal.bitsize) + "@" + str(endianess) + str(signed) + " (" + str(signal.factor) + "," + str(signal.offset) + ")" + " [" + str(signal.minvalue) + "|" + str(signal.maxvalue) + "]" + " " + '"' + str(signal.unit) + '"' + " " + "Vector__XXX" + "\n")
				signal_offset = signal_offset + int(signal.bitsize)

			fo.write('\n')
	fo.write('\n')
	fo.write('\n')
	fo.write('BA_DEF_  "BusType" STRING ;\n')
	fo.write('BA_DEF_DEF_  "BusType" "";\n')
	for entry in float_footer:
		fo.write(entry)
	fo.write('\n')
