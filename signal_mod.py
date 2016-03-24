class signal:
	def __init__(self):
		self.name = ""
		self.id = 0
		self.type = ""
		self.init_value = 0
		self.factor = 0
		self.offset = 0
		self.unit = ""

	def set_params(self,signal_name, signal_id, datatype, init_value, factor, offset, unit):
		self.name = signal_name
		self.id = signal_id
		self.type = datatype
		self.init_value = init_value
		self.factor = factor
		self.offset = offset
		self.unit = unit

	def print_callback(self, fo):
		fo.write("#ifndef {}_callback\n".format(self.name))
		fo.write("#\tdefine {}_callback NULL\n".format(self.name))
		fo.write("#endif\n")

	def print_enum(self, fo):
		fo.write("\t{},\n".format(self.name))

	def print_para_macro(self, fo, last):
		if(last):
			fo.write("\tCAN_PARA_MACRO({}, sizeof({}), {}, {}_callback)\n".format(self.name, self.type, self.init_value, self.name))
		else:
			fo.write("\tCAN_PARA_MACRO({}, sizeof({}), {}, {}_callback),\n".format(self.name, self.type, self.init_value, self.name))

	def print_definition(self, fo, byte_pos, last, little_endian):
		fo.write("\t\t\t{\n")
		fo.write("\t\t\t\t{},       /* Signal ID */\n".format(self.name))


		if(little_endian):
			fo.write("\t\t\t\t{}|CANFRM_LITTLE_ENDIAN				       /* Byte Position */\n".format(byte_pos))
		else:
			fo.write("\t\t\t\t{}				       /* Byte Position */\n".format(byte_pos))

		if(last):
			fo.write("\t\t\t}\n")
		else:
			fo.write("\t\t\t},\n")


	def print_debug(self):
		print self.name
		print self.id
		print self.type
		print self.init_value
		print self.factor
		print self.offset
		print self.unit
