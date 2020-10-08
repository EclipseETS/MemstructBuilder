class boards:

	def __init__(self):
		self.name = ""
		self.offset = 0
		self.extend = 0
		self.little_endian = 0
		self.message = []
		self.message_cnt = 0

	def set_params(self, board_name, board_offset, board_extend, board_endian):
		self.name = board_name
		self.offset = board_offset
		self.extend = board_extend
		self.little_endian = board_endian

	def add_message(self, message):
		self.message.append(message)
		self.message_cnt += 1
		
	def print_header(self):
		return (
			f"/*******************************************************************/\n"
			f"/*      {self.name}      */\n"
			f"/********************************************************************/\n"
		)

	def print_callback(self):
		str = ""
		for mes in self.message:
			str += mes.print_callback()
		return str
			
	def print_enum(self):
		if self.extend:
			return("        ID_OFFSET_{} = 0x{:02X}L | CANFRM_EXTENDED_ID,\n".format(self.name, self.offset))
		else:
			return("        ID_OFFSET_{} = 0x{:02X},\n".format(self.name, self.offset))

	def print_signal_enum(self):
		str = ""
		for mes in self.message:
			str += mes.print_signal_enum()
		return str

	def print_message_enum(self):
		last_id = -100
		str = ""
		for mes in self.message:
			str += mes.print_enum(last_id)
			last_id = mes.id
		return (str + f"        M_MAX_{self.name} = {self.message_cnt},\n")

	def print_message_enum_telemetry(self):
		last_id = -100
		str = ""
		for mes in self.message:
			str += mes.print_enum_full_id(last_id, self)
			last_id = mes.id + self.offset;
		return str

	def print_para_macro(self, last):
		str = ""
		for mes in self.message:
			str += mes.print_para_macro(last)
		return str

	def print_txrx(self):
		return (
			f"#ifndef M_{self.name}_TXRX\n"
			f"#        define M_{self.name}_TXRX CANMSG_RX\n"
			f"#endif\n"
		)

	def print_message_def(self):
		str = ""
		for mes in self.message:
			str += mes.print_message_def(self.name, self.little_endian)
		return str

	def print_message_def_telemetry(self):
		str = ""
		for mes in self.message:
			str += mes.print_message_def_telemetry(self.name, self.little_endian)
		return str

	def print_debug(self):
		print (self.name)
		print (self.offset)
		print (self.extend)
		print (self.little_endian)
		print (self.message_cnt)

		for mes in self.message:
			mes.print_debug()
