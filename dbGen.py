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
			dlc = 0
			signal_offset = 0
			for signal in message.signal:
				dlc = dlc + (int(signal.bitsize) / 8)
			fo.write("\n\n" + "BO_" + " " + str(board.offset + message.id) + " " + str(message.name) + ": " + str(dlc) + " " + "Vector__XXX" + "\n")
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

		
