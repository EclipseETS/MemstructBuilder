#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

m_name = \
[ \
["M_DRIVER_MOTOR_CMD", "M_DRIVER_POWER_CMD"], \
["M_DRIVE_ID", "M_DRIVE_STATUS", "M_DRIVE_BUS", "M_DRIVE_VELOCITY", "M_DRIVE_PHASE_CURRENT", "M_DRIVE_BEMF", "M_DRIVE_15V", "M_DRIVE_33V_19V", "M_DRIVE_HEATSINK_MOTOR_TEMP", "M_DRIVE_DSP_TEMP", "M_DRIVE_ODOMETER_AMPHOUR"], \
["M_BMS_HEARTBEAT", "M_BMS_CMU1_ID_TEMP", "M_BMS_CMU1_CELL_0TO3", "M_BMS_CMU1_CELL_4TO7", "M_BMS_CMU2_ID_TEMP", "M_BMS_CMU2_CELL_0TO3", "M_BMS_CMU2_CELL_4TO7", "M_BMS_CMU3_ID_TEMP", "M_BMS_CMU3_CELL_0TO3", "M_BMS_CMU3_CELL_4TO7", "M_BMS_CMU4_ID_TEMP", "M_BMS_CMU4_CELL_0TO3", "M_BMS_CMU4_CELL_4TO7", "M_BMS_SOC ", "M_BMS_BALANCE_SOC", "M_BMS_CHARGER_CONTROL", "M_BMS_PRECHARGE_STATUS", "M_BMS_MIN_MAX_CELL_VOLTAGE", "M_BMS_MIN_MAX_CELL_TEMP", "M_BMS_CURRENT_VOLTAGE", "M_BMS_PACK_STATUS", "M_BMS_FAN_STATUS", "M_BMS_PACK_EXTENDED_STATUS"], \
["M_FLASHERS_STATUS", "M_FLASHERS_PEDAL"], \
["M_VOLANT_STATUS", "M_VOLANT_CTRL"], \
["M_INSTRU_STATUS", "M_INSTRU_GPS", "M_INSTRU_TIME", "M_INSTRU_INCL", "M_INSTRU_CMD", "M_INSTRU_ACC"], \
["M_POWERSUPPLY_STATUS", "M_POWERSUPPLY_CAN", "M_POWERSUPPLY_HP", "M_POWERSUPPLY_AUX"] \
]

s_name = \
[ \
["S_DRIVER_MOTOR_CURRENT", "S_DRIVER_MOTOR_VELOCITY", "S_DRIVER_BUS_CURRENT"], \
["S_DRIVE_SERIAL", "S_DRIVE_ID", "S_DRIVE_RX_ERR_CNT", "S_DRIVE_TX_ERR_CNT", "S_DRIVE_ACTIVE_MOTOR", "S_DRIVE_ERR_FLAGS", "S_DRIVE_LIMIT_FLAGS", "S_DRIVE_BUS_CURRENT", "S_DRIVE_BUS_VOLTAGE", "S_DRIVE_VEHICLE_VELOCITY", "S_DRIVE_MOTOR_VELOCITY", "S_DRIVE_PHASE_C_CURRENT", "S_DRIVE_PHASE_B_CURRENT", "S_DRIVE_BEMFD", "S_DRIVE_BEMFQ", "S_DRIVE_15V", "S_DRIVE_3_3V", "S_DRIVE_1_9V", "S_DRIVE_HEATSINK_TEMP", "S_DRIVE_MOTOR_TEMP", "S_DRIVE_DSP_TEMP", "S_DRIVE_DCBUS_AMPHOUR", "S_DRIVE_ODOMETER"], \
["S_BMS_DEVICEID", "S_BMS_SERIAL", "S_BMS_CMU1_SERIAL", "S_BMS_CMU1_PCB_TEMP", "S_BMS_CMU1_CELL_TEMP", "S_BMS_CMU1_CELL0_VOLTAGE", "S_BMS_CMU1_CELL1_VOLTAGE", "S_BMS_CMU1_CELL2_VOLTAGE", "S_BMS_CMU1_CELL3_VOLTAGE", "S_BMS_CMU1_CELL4_VOLTAGE", "S_BMS_CMU1_CELL5_VOLTAGE", "S_BMS_CMU1_CELL6_VOLTAGE", "S_BMS_CMU1_CELL7_VOLTAGE", "S_BMS_CMU2_SERIAL", "S_BMS_CMU2_PCB_TEMP", "S_BMS_CMU2_CELL_TEMP", "S_BMS_CMU2_CELL0_VOLTAGE", "S_BMS_CMU2_CELL1_VOLTAGE", "S_BMS_CMU2_CELL2_VOLTAGE", "S_BMS_CMU2_CELL3_VOLTAGE", "S_BMS_CMU2_CELL4_VOLTAGE", "S_BMS_CMU2_CELL5_VOLTAGE", "S_BMS_CMU2_CELL6_VOLTAGE", "S_BMS_CMU2_CELL7_VOLTAGE", "S_BMS_CMU3_SERIAL", "S_BMS_CMU3_PCB_TEMP", "S_BMS_CMU3_CELL_TEMP", "S_BMS_CMU3_CELL0_VOLTAGE", "S_BMS_CMU3_CELL1_VOLTAGE", "S_BMS_CMU3_CELL2_VOLTAGE", "S_BMS_CMU3_CELL3_VOLTAGE", "S_BMS_CMU3_CELL4_VOLTAGE", "S_BMS_CMU3_CELL5_VOLTAGE", "S_BMS_CMU3_CELL6_VOLTAGE", "S_BMS_CMU3_CELL7_VOLTAGE", "S_BMS_CMU4_SERIAL", "S_BMS_CMU4_PCB_TEMP", "S_BMS_CMU4_CELL_TEMP", "S_BMS_CMU4_CELL0_VOLTAGE", "S_BMS_CMU4_CELL1_VOLTAGE", "S_BMS_CMU4_CELL2_VOLTAGE", "S_BMS_CMU4_CELL3_VOLTAGE", "S_BMS_CMU4_CELL4_VOLTAGE", "S_BMS_CMU4_CELL5_VOLTAGE", "S_BMS_CMU4_CELL6_VOLTAGE", "S_BMS_CMU4_CELL7_VOLTAGE", "S_BMS_SOC_AH", "S_BMS_SOC_POURCENT", "S_BMS_BALANCING_SOC_AH", "S_BMS_BALANCING_SOC_POURCENT", "S_BMS_CHARGER_CELL_VOLTAGE_ERROR", "S_BMS_CHARGER_CELL_TEMP_MARGIN", "S_BMS_CHARGER_CELL_DISCHARGE_VOLTAGE_ERROR", "S_BMS_TOTAL_CAPACITY_AH", "S_BMS_PRECHARGE_CONTACTOR_STATUS", "S_BMS_PRECHARGE_STATE", "S_BMS_CONTACTOR_VOLTAGE_SUPLY", "S_BMS_PRECHARGE_TIMER_STATUS", "S_BMS_PRECHARGE_TIMER_COUNT", "S_BMS_MIN_CELL_VOLTAGE", "S_BMS_MAX_CELL_VOLTAGE", "S_BMS_MIN_VOLTAGE_CELL_CMU_NUMBER", "S_BMS_MIN_VOLTAGE_CELL_NUMBER", "S_BMS_MAX_VOLTAGE_CELL_CMU_NUMBER", "S_BMS_MAX_VOLTAGE_CELL_NUMBER", "S_BMS_MIN_CELL_TEMP", "S_BMS_MAX_CELL_TEMP", "S_BMS_MIN_TEMP_CELL_CMU_NUMBER", "S_BMS_MAX_TEMP_CELL_CMU_NUMBER", "S_BMS_TOTAL_VOLTAGE", "S_BMS_TOTAL_CURRENT", "S_BMS_BALANCE_THRESHOLD_RISING", "S_BMS_BALANCE_THRESHOLD_FALLING", "S_BMS_PACK_STATUS", "S_BMS_CMU_COUNT", "S_BMS_BMU_FIRMWARE", "S_BMS_FAN0_SPEED", "S_BMS_FAN1_SPEED", "S_BMS_FAN_CONTACTOR_CONSUMPTION", "S_BMS_CMU_CONSUMPTION", "S_BMS_EXTENDED_STATUS", "S_BMS_BMU_HARDWARE_VERSION", "S_BMS_BMU_MODELID"], \
["S_FLASHERS_STATUS", "S_FLASHERS_OSTICK", "S_FLASHERS_BREAK", "S_FLASHERS_ACCL"], \
["S_VOLANT_STATUS", "S_VOLANT_OSTICK", "S_VOLANT_OPMODE", "S_VOLANT_BUTTON"], \
["S_INSTRU_STATUS", "S_INSTRU_OSTICK", "S_INSTRU_GPSLAT", "S_INSTRU_GPSLONG", "S_INSTRU_TIME", "S_INSTRU_DATE", "S_INSTRU_TEMPINCL", "S_INSTRU_INCL", "S_INSTRU_CMD", "S_INSTRU_ACC_X", "S_INSTRU_ACC_Y", "S_INSTRU_ACC_Z"], \
["S_POWERSUPPLY_STATUS", "S_POWERSUPPLY_OSTICK", "S_POWERSUPPLY_12V_CAN_COURANT", "S_POWERSUPPLY_12V_CAN_VOLTAGE", "S_POWERSUPPLY_12V_HP_COURANT", "S_POWERSUPPLY_12V_HP_VOLTAGE", "S_POWERSUPPLY_12V_AUX_COURANT", "S_POWERSUPPLY_12V_AUX_VOLTAGE",] \
]

board_index = 0
m_name_index = 0
s_name_index = 0
initial_value = "0"
deviceitem_list = []

# Create XML output file
fo = open("memstruct_entry.txt", "w+")

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("protocolV8.xml")
collection = DOMTree.documentElement

# Get all the movies in the collection
devices = collection.getElementsByTagName("device")

# Print detail of each movie.
for device in devices:
	m_name_index = 0
	s_name_index = 0
	print "*****device*****"
	#id_board = device.getAttribute("id")
	#print "id:=%s" % id_board
	name = device.getAttribute("name")
	print "name:=%s" % name

	trames = device.getElementsByTagName('trame')
	for trame in trames:
		print "*****trame*****"
		identifier = trame.getAttribute("identifier")
		print "identifier=%s" % identifier
		type = trame.getAttribute("type")
		print "type=%s" % type
		msg_offset = "0x" + identifier[1:3].upper()
		board_id = "0x" + identifier[0] + "00"
		if (trame == trames[0]):
			if (board_id == "0x100" or board_id == "0x200" or board_id == "0x300"):
				is_extended = "0"
				is_little_endian = "1"
			else:
				is_extended = "1"
				is_little_endian = "0"

			if board_id == "0x100":
				board_name = "DRIVER"
				board_index = 0
			elif board_id == "0x200":
				board_name = "DRIVE"
				board_index = 1
			elif board_id == "0x300":
				board_name = "BMS"
				board_index = 2
			elif board_id == "0x400":
				board_name = "FLASHERS"
				board_index = 3
			elif board_id == "0x500":
				board_name = "VOLANT"
				board_index = 4
			elif board_id == "0x600":
				board_name = "INSTRU"
				board_index = 5
			elif board_id == "0x700":
				board_name = "POWERSUPPLY"
				board_index = 6

			fo.write("\nb:" + board_name + ", " + board_id + ", " + is_extended + ", " + is_little_endian + "\n")
		fo.write("\n" + "m:" + m_name[board_index][m_name_index] + ", " + msg_offset + "\n")
		m_name_index = m_name_index + 1

		deviceitems = trame.getElementsByTagName('deviceitem')
		for deviceitem in deviceitems:
			print "*****deviceitem*****"
			id = deviceitem.getAttribute("id")
			print "id=%s" % id
			unit = deviceitem.getElementsByTagName('unit')[0].childNodes[0].data
			print "unit=%s" % unit
			bitsize = deviceitem.getElementsByTagName('bitsize')[0].childNodes[0].data
			print "bitsize=%s" % bitsize
			minvalue = deviceitem.getElementsByTagName('minvalue')[0].childNodes[0].data
			print "minvalue=%s" % minvalue
			maxvalue = deviceitem.getElementsByTagName('maxvalue')[0].childNodes[0].data
			print "maxvalue=%s" % maxvalue
			resolution = deviceitem.getElementsByTagName('resolution')[0].childNodes[0].data
			print "resolution=%s" % resolution
			factor = deviceitem.getElementsByTagName('factor')[0].childNodes[0].data
			print "factor=%s" % factor
			offset = deviceitem.getElementsByTagName('offset')[0].childNodes[0].data
			print "offset=%s" % offset
			signed = deviceitem.getElementsByTagName('signed')[0].childNodes[0].data
			print "signed=%s" % signed
			isFloat = deviceitem.getElementsByTagName('isFloat')[0].childNodes[0].data
			print "isFloat=%s" % isFloat
			if (isFloat == "true"):
				data_type = "F"
			else:
				if (bitsize == "8" and signed == "true"):
					data_type = "8"
				elif (bitsize == "16" and signed == "true"):
					data_type = "16"
				elif (bitsize == "32" and signed == "true"):
					data_type = "32"
				elif (bitsize == "8" and signed == "false"):
					data_type = "U8"
				elif (bitsize == "16" and signed == "false"):
					data_type = "U16"
				elif (bitsize == "32" and signed == "false"):
					data_type = "U32"

			deviceitem_list.append("s:" + s_name[board_index][s_name_index] + ", " + data_type + ", " + initial_value + ", " + factor + ", " + offset + ", " + unit + ", " + minvalue + ", " + maxvalue + "\n")
			s_name_index = s_name_index + 1

		if (is_little_endian == "1"):
			for item in reversed(deviceitem_list):
				fo.write(item)
		else:
			for item in deviceitem_list:
				fo.write(item)

		del deviceitem_list[:]
