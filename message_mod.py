class Message:

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
		callbacks = []
		for sig in self.signal:
			callbacks.append(sig.print_callback())
		string = '\n'.join(callbacks)
		return string

	def print_signal_enum(self):
		signal_enum = []
		for sig in self.signal:
			signal_enum.append(sig.print_enum())
		string = ',\n'.join(signal_enum)
		return string

	def print_enum(self, last_id):
		if last_id + 1 == self.id:
			string = f"        {self.name},\n"
		else:
			string = f"        {self.name} = {self.id},\n"
		last_id = self.id
		return string

	def print_enum_full_id(self, last_id, board):
		if last_id + 1 == board.offset + self.id:
			string = f"        {self.name}"
		elif self.id == 0:
			string = f"        {self.name} = ID_OFFSET_{board.name}"
		else:
			string = f"        {self.name} = {self.id}+ID_OFFSET_{board.name}"
		last_id = board.offset + self.id
		return string

	def print_para_macro(self, last):
		cnt = len(self.signal)
		para_macro = []
		for index, sig in enumerate(self.signal, start=1):
			if last and cnt == index:
				para_macro.append(sig.print_para_macro(1))
			else:
				para_macro.append(sig.print_para_macro(0))
		string = ',\n'.join(para_macro)
		return string

	def print_message_def(self, board_name, little_endian):
		string = (
			f"        {{\n"
			f"                ID_OFFSET_{board_name} + {self.name}, /* CAN-Identifier */\n"
			f"                M_{board_name}_TXRX, /* Message Type */\n"
			f"                "
			f""
		)
		
		for index, sig in enumerate(self.signal, start=1):
			if index == self.signal_cnt:
				string += f"sizeof({sig.type}),"
			else:
				string += f"sizeof({sig.type}) + "
		
		string += (
			f" /* DLC of Message */\n"
			f"                {self.signal_cnt}, /* No. of Links */\n"
			f"                {{\n"
		)

		byte_pos = "0"

		for index, sig in enumerate(self.signal, start=1):
			if index == self.signal_cnt:
				string += sig.print_definition(byte_pos, 1, little_endian)
			else:
				string += sig.print_definition(byte_pos, 0, little_endian)
			byte_pos = byte_pos + f" + sizeof({sig.type})"

		string += (
			f"                }}\n"
			f"        }}"
		)
		return string

	def print_message_def_telemetry(self, little_endian):
		signals_str = ""
		for index, sig in enumerate(self.signal, start=1):
			if index == self.signal_cnt:
				signals_str += f"sizeof({sig.type}),"
			else:
				signals_str += f"sizeof({sig.type}) + "
		string = (
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
		
		for index, sig in enumerate(self.signal, start=1):
			if index == self.signal_cnt:
				string += sig.print_definition_telemetry(byte_pos, 1, little_endian)
			else:
				string += sig.print_definition_telemetry(byte_pos, 0, little_endian)
			byte_pos = byte_pos + f" + sizeof({sig.type})"
		
		string += (
			f"                        }}\n"
			f"                }}\n"
			f"        }}"
		)
		return string
