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

	for board in board_list:
		for message in board.message:
			fo.write("\n\n" + "BO_" + " " + str(message.id) + " " + str(message.name) + ": " + "DLC" + " " + "Vector__XXX" + "\n")
			for signal in message.signal:
				fo.write(" SG_" + " " + str(signal.name) + " : " + "0|" + str(signal.bitsize) + '@1- (1|0) [2|4] "V" Vector__XXX' + "\n")
				# ET.SubElement(deviceitem, "unit").text = str(signal.unit)
				# ET.SubElement(deviceitem, "bitsize").text = str(signal.bitsize)
				# ET.SubElement(deviceitem, "minvalue").text = str(signal.minvalue)
				# ET.SubElement(deviceitem, "maxvalue").text = str(signal.maxvalue)
				# ET.SubElement(deviceitem, "resolution").text = "1"
				# ET.SubElement(deviceitem, "factor").text = str(signal.factor)
				# ET.SubElement(deviceitem, "offset").text = str(signal.offset)
				# ET.SubElement(deviceitem, "signed").text = str(signal.signed)
				# ET.SubElement(deviceitem, "isFloat").text = str(signal.float)
