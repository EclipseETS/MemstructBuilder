class Board:

	def __init__(self):
		self.name = ""
		self.offset = 0
		self.extend = 0
		self.little_endian = 0
		self.message = []
		self.message_cnt = 0
		self.header_width = 70

	def set_params(self, board_name, board_offset, board_extend, board_endian):
		self.name = board_name
		self.offset = board_offset
		self.extend = board_extend
		self.little_endian = board_endian

	def add_message(self, message):
		self.message.append(message)
		self.message_cnt += 1
		
	def print_header(self):
		string = '/' + '*' * self.header_width + '/\n'
		string += f'/*{self.name: ^{self.header_width - 2}}*/\n'
		string += '/' + '*' * self.header_width + '/\n'
		return string

	def print_callback(self):
		callbacks = []
		for mes in self.message:
			callbacks.append(mes.print_callback())
		string = '\n'.join(callbacks)
		return string
			
	def print_enum(self):
		if self.extend:
			return "        ID_OFFSET_{} = {:#02x}L | CANFRM_EXTENDED_ID".format(self.name, self.offset)
		else:
			return "        ID_OFFSET_{} = {:#02x}".format(self.name, self.offset)

	def print_signal_enum(self):
		signal_enum = []
		for mes in self.message:
			signal_enum.append(mes.print_signal_enum())
		string = ',\n'.join(signal_enum)
		return string

	def print_message_enum(self):
		last_id = -100
		string = ""
		for mes in self.message:
			string += mes.print_enum(last_id)
			last_id = mes.id
		return string + f"        M_MAX_{self.name} = {self.message_cnt}"

	def print_message_enum_telemetry(self):
		last_id = -100
		message_enums = []
		for mes in self.message:
			message_enums.append(mes.print_enum_full_id(last_id, self))
			last_id = mes.id + self.offset
		string = ',\n'.join(message_enums)
		return string

	def print_para_macro(self, last):
		para_strings = []
		for mes in self.message:
			para_strings.append(mes.print_para_macro(last))
		string = ',\n'.join(para_strings)
		return string

	def print_txrx(self):
		return (
			f"#ifndef M_{self.name}_TXRX\n"
			f"#        define M_{self.name}_TXRX CANMSG_RX\n"
			f"#endif\n"
		)

	def print_message_def(self):
		message_strings = []
		for mes in self.message:
			message_strings.append(mes.print_message_def(self.name, self.little_endian))
		string = ',\n'.join(message_strings)
		return string

	def print_message_def_telemetry(self):
		message_defs = []
		for mes in self.message:
			message_defs.append(mes.print_message_def_telemetry(self.little_endian))
		string = ',\n'.join(message_defs)
		return string
