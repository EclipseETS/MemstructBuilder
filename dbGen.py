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

	for board in board_list:
		for message in board.message:
			dlc = 0
			signal_offset = 0
			for signal in message.signal:
				dlc = dlc + (int(signal.bitsize) / 8)
			fo.write("BO_" + " " + str(board.offset + message.id) + " " + str(message.name) + ": " + str(dlc) + " " + "Vector__XXX" + "\n")
			for signal in message.signal:
				if (signal.signed == "true"):
					signed = "-"
				else:
					signed = "+"
				fo.write(" SG_" + " " + str(signal.name) + " : " + str(signal_offset) + "|" + str(signal.bitsize) + "@1" + str(signed) + " (" + str(signal.factor) + "," + str(signal.offset) + ")" + " [" + str(signal.minvalue) + "|" + str(signal.maxvalue) + "]" + " " + '"' + str(signal.unit) + '"' + " " + "Vector__XXX" + "\n")
				signal_offset = signal_offset + int(signal.bitsize)
				# ET.SubElement(deviceitem, "unit").text = str(signal.unit)
				# ET.SubElement(deviceitem, "bitsize").text = str(signal.bitsize)
				# ET.SubElement(deviceitem, "minvalue").text = str(signal.minvalue)
				# ET.SubElement(deviceitem, "maxvalue").text = str(signal.maxvalue)
				# ET.SubElement(deviceitem, "resolution").text = "1"
				# ET.SubElement(deviceitem, "factor").text = str(signal.factor)
				# ET.SubElement(deviceitem, "offset").text = str(signal.offset)
				# ET.SubElement(deviceitem, "signed").text = str(signal.signed)
				# ET.SubElement(deviceitem, "isFloat").text = str(signal.float)
			fo.write('\n')
