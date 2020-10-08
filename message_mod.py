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

	def print_callback(self):
		str = ""
		for sig in self.signal:
			str += sig.print_callback()
		return str

	def print_signal_enum(self):
		str = ""
		for sig in self.signal:
			str += sig.print_enum()
		return str

	def print_enum(self, last_id):
		if (last_id + 1 == self.id):
			str = (f"        {self.name},\n")
		else:
			str = (f"        {self.name} = {self.id},\n")
		last_id = self.id
		return str

	def print_enum_full_id(self, last_id, board):
		if (last_id + 1 == board.offset + self.id):
			str = (f"        {self.name},\n")
		elif (self.id == 0):
			str = (f"        {self.name} = ID_OFFSET_{board.name},\n")
		else:
			str = (f"        {self.name} = {self.id}+ID_OFFSET_{board.name},\n")
		last_id = board.offset + self.id
		return str

	def print_para_macro(self, last):
		cnt = len(self.signal)
		str = ""
		for index, sig in enumerate(self.signal, start = 1):
			if(last and cnt == index):
				str += sig.print_para_macro(1)
			else:
				str += sig.print_para_macro(0)
		return str

	def print_message_def(self, board_name, little_endian):
		str = (
			f"        {{\n"
			f"                ID_OFFSET_{board_name} + {self.name}, /* CAN-Identifier */\n"
			f"                M_{board_name}_TXRX, /* Message Type */\n"
			f"                "
			f""
		)
		
		for index, sig in enumerate(self.signal, start = 1):
			if(index == self.signal_cnt):
				str += (f"sizeof({sig.type}),")
			else:
				str += (f"sizeof({sig.type}) + ")
		
		str += (
			f" /* DLC of Message */\n"
			f"                {self.signal_cnt}, /* No. of Links */\n"
			f"                {{\n"
		)

		byte_pos = "0"

		for index, sig in enumerate(self.signal, start = 1):
			if(index == self.signal_cnt):
				str += sig.print_definition(byte_pos, 1, little_endian)
			else:
				str += sig.print_definition(byte_pos, 0, little_endian)
			byte_pos = byte_pos + f" + sizeof({sig.type})"

		str += (
			f"                }}\n"
			f"        }},\n"
		)
		return str

	def print_message_def_telemetry(self, board_name, little_endian):
		signals_str = ""
		for index, sig in enumerate(self.signal, start = 1):
			if(index == self.signal_cnt):
				signals_str += f"sizeof({sig.type}),"
			else:
				signals_str += f"sizeof({sig.type}) + "
		str = (
			f"        {{\n"
			f"                {self.name}, /* CAN-Identifier */\n"
			f"                {{\n"
			f"                        {self.name}, /* CAN-Identifier */\n"
			f"                        "
			f"{signals_str}"
			f" /* DLC of Message */\n"
			f"                        "
			f"\"{self.name}\","
			f" /* Name of Message */\n"
			f"                        {self.signal_cnt}, /* No. of Links */\n"
			f"                        {{\n"
		)

		byte_pos = f"0"
		
		for index, sig in enumerate(self.signal, start = 1):
			if(index == self.signal_cnt):
				str += sig.print_definition_telemetry(byte_pos, 1, little_endian)
			else:
				str += sig.print_definition_telemetry(byte_pos, 0, little_endian)
			byte_pos = byte_pos + f" + sizeof({sig.type})"
		
		str += (
			f"                        }}\n"
			f"                }}\n"
			f"        }},\n"
		)
		return str

	def print_debug(self):
		print (self.name)
		print (self.id)
		print (self.signal_cnt)

		for sig in self.signal:
			sig.print_debug()
