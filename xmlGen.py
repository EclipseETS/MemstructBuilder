import xml.etree.cElementTree as ET
from xml.dom import minidom
import sys
import os
from message_mod import message
from signal_mod import signal
from board_mod import boards

def generate(board_list):

	try:
		os.remove("output/protocolV9.xml")
	except:
		pass

	fo = open("output/protocolV9.xml", "w+")

	att = {"xmlnsl": "http://eclipse.etsmtl.ca", "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", "xsi:schemaLocation": "http://eclipse.etsmtl.ca protocolV8Schema.xsd"}
	root = ET.Element("char", att)

	for board in board_list:
		att = {"id": (str(format(board.offset, '02x')))[0:1], "name": board.name}
		device = ET.SubElement(root, "device", att)

		cnt = 0
		for message in board.message:
			att = {"identifier": str(format(board.offset + message.id, '02x')), "type": "0"} #a verifier
			trame = ET.SubElement(device, "trame", att)

			for signal in message.signal:
				att = {"id": str(cnt), "name": signal.name}
				deviceitem = ET.SubElement(trame, "deviceitem", att)
				ET.SubElement(deviceitem, "unit").text = str(signal.unit)
				ET.SubElement(deviceitem, "bitsize").text = str(signal.bitsize)
				ET.SubElement(deviceitem, "minvalue").text = str(signal.minvalue)
				ET.SubElement(deviceitem, "maxvalue").text = str(signal.maxvalue)
				ET.SubElement(deviceitem, "resolution").text = "1"
				ET.SubElement(deviceitem, "factor").text = str(signal.factor)
				ET.SubElement(deviceitem, "offset").text = str(signal.offset)
				ET.SubElement(deviceitem, "signed").text = str(signal.signed)
				ET.SubElement(deviceitem, "isFloat").text = str(signal.float)
				cnt += 1
				
	rough = ET.tostring(root, 'utf-8')
	reparsed = minidom.parseString(rough)
	fo.write(reparsed.toprettyxml(indent="\t"))
