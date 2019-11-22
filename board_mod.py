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

	def print_header(self, fo):
		fo.write("/*******************************************************************/\n")
		fo.write("/*                                                        {}                                                                        */\n".format(self.name))
		fo.write("/********************************************************************/\n")

	def print_callback(self, fo):
		for mes in self.message:
			mes.print_callback(fo)

	def print_enum(self, fo):
		if self.extend:
			fo.write("        ID_OFFSET_{} = 0x{:02X}L | CANFRM_EXTENDED_ID,\n".format(self.name, self.offset))
		else:
			fo.write("        ID_OFFSET_{} = 0x{:02X},\n".format(self.name, self.offset))

	def print_signal_enum(self, fo):
		for mes in self.message:
			mes.print_signal_enum(fo)

	def print_message_enum(self, fo):
		last_id = -100
		for mes in self.message:
			mes.print_enum(fo, last_id)
			last_id = mes.id
		fo.write("        M_MAX_{} = {},\n".format(self.name, self.message_cnt))

	def print_para_macro(self, fo, last):
		for mes in self.message:
			mes.print_para_macro(fo, last)

	def print_txrx(self, fo):
		fo.write("#ifndef M_{}_TXRX\n".format(self.name))
		fo.write("#        define M_{}_TXRX CANMSG_RX\n".format(self.name))
		fo.write("#endif\n")

	def print_message_def(self, fo):
		for mes in self.message:
			mes.print_message_def(fo, self.name, self.little_endian)

	def print_debug(self):
		print self.name
		print self.offset
		print self.extend
		print self.little_endian
		print self.message_cnt

		for mes in self.message:
			mes.print_debug()
