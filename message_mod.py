class message:

	def __init__(self):
		self.name = ""
		self.id = 0
		self.signal = []
		self.signal_cnt = 0

	def set_params(self, message_name, message_id):
		self.name = message_name
		self.id = message_id

	def add_signal(self, signal):
		self.signal.append(signal)
		self.signal_cnt += 1

	def print_callback(self, fo):
		for sig in self.signal:
			sig.print_callback(fo)

	def print_signal_enum(self, fo):
		for sig in self.signal:
			sig.print_enum(fo)

	def print_enum(self, fo, last_id):
		if (last_id + 1 == self.id):
			fo.write("        {},\n".format(self.name))
		else:
			fo.write("        {} = {},\n".format(self.name, self.id))
		last_id = self.id

	def print_enum_full_id(self, fo, last_id, board):
		if (last_id + 1 == board.offset + self.id):
			fo.write("        {},\n".format(self.name))
		elif (self.id == 0):
			fo.write("        {} = ID_OFFSET_{},\n".format(self.name, board.name))
		else:
			fo.write("        {} = {}+ID_OFFSET_{},\n".format(self.name, self.id, board.name))
		last_id = board.offset + self.id

	def print_para_macro(self, fo, last):
		cnt = len(self.signal)
		for index, sig in enumerate(self.signal, start = 1):
			if(last and cnt == index):
				sig.print_para_macro(fo, 1)
			else:
				sig.print_para_macro(fo, 0)

	def print_message_def(self, fo, board_name, little_endian):
		fo.write("        {\n")
		fo.write("                ID_OFFSET_{} + {}, /* CAN-Identifier */\n".format(board_name, self.name))
		fo.write("                M_{}_TXRX, /* Message Type */\n".format(board_name))

		fo.write("                ")
		for index, sig in enumerate(self.signal, start = 1):
			if(index == self.signal_cnt):
				fo.write("sizeof({}),".format(sig.type))
			else:
				fo.write("sizeof({}) + ".format(sig.type))
		fo.write(" /* DLC of Message */\n")

		fo.write("                {}, /* No. of Links */\n".format(self.signal_cnt))
		fo.write("                {\n")

		byte_pos = "0"

		for index, sig in enumerate(self.signal, start = 1):
			if(index == self.signal_cnt):
				sig.print_definition(fo, byte_pos, 1, little_endian)
			else:
				sig.print_definition(fo, byte_pos, 0, little_endian)
			byte_pos = byte_pos + " + sizeof({})".format(sig.type)

		fo.write("                }\n")
		fo.write("        },\n")

	def print_message_def_telemetry(self, fo, board_name, little_endian):
		fo.write("        {\n")
		fo.write("                {}, /* CAN-Identifier */\n".format(self.name))
		fo.write("                {\n")
		fo.write("                        {}, /* CAN-Identifier */\n".format(self.name))
		fo.write("                        ")
		for index, sig in enumerate(self.signal, start = 1):
			if(index == self.signal_cnt):
				fo.write("sizeof({}),".format(sig.type))
			else:
				fo.write("sizeof({}) + ".format(sig.type))
		fo.write(" /* DLC of Message */\n")
		fo.write("                        ")
		fo.write("\"{}\",".format(self.name))
		fo.write(" /* Name of Message */\n")
		fo.write("                        {}, /* No. of Links */\n".format(self.signal_cnt))
		fo.write("                        {\n")

		byte_pos = "0"

		for index, sig in enumerate(self.signal, start = 1):
			if(index == self.signal_cnt):
				sig.print_definition_telemetry(fo, byte_pos, 1, little_endian)
			else:
				sig.print_definition_telemetry(fo, byte_pos, 0, little_endian)
			byte_pos = byte_pos + " + sizeof({})".format(sig.type)

		fo.write("                        }\n")
		fo.write("                }\n")
		fo.write("        },\n")

	def print_debug(self):
		print (self.name)
		print (self.id)
		print (self.signal_cnt)

		for sig in self.signal:
			sig.print_debug()
