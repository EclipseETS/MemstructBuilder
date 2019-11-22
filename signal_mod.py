class signal:
	def __init__(self):
		self.name = ""
		self.id = 0
		self.type = ""
		self.bitsize = 0
		self.init_value = 0
		self.factor = 0
		self.offset = 0
		self.unit = ""
		self.minvalue = 0
		self.maxvalue = 0
		self.signed = "false"
		self.float = "false"

	def set_params(self,signal_name, signal_id, datatype, init_value, factor, offset, unit, minvalue, maxvalue, bitsize, issigned, isfloat):
		self.name = signal_name
		self.id = signal_id
		self.type = datatype
		self.bitsize = bitsize
		self.init_value = init_value
		self.factor = factor
		self.offset = offset
		self.unit = unit
		self.minvalue = minvalue
		self.maxvalue = maxvalue
		self.signed = issigned
		self.float = isfloat

	def print_callback(self, fo):
		fo.write("#ifndef {}_callback\n".format(self.name))
		fo.write("#        define {}_callback NULL\n".format(self.name))
		fo.write("#endif\n")

	def print_enum(self, fo):
		fo.write("        {},\n".format(self.name))

	def print_para_macro(self, fo, last):
		if(last):
			fo.write("        CAN_PARA_MACRO({}, sizeof({}), {}, {}_callback),\n\n".format(self.name, self.type, self.init_value, self.name))
			fo.write("#ifdef E92_USE_CUSTOM_MEMSTRUCT\n")
			fo.write("/*******************************************************************/\n")
			fo.write("/*                                                    CUSTOM CAN                                                         */\n")
			fo.write("/********************************************************************/\n")
			fo.write("        CUSTOM_CAN_SIG,\n")
			fo.write("#endif\n\n")
		else:
			fo.write("        CAN_PARA_MACRO({}, sizeof({}), {}, {}_callback),\n".format(self.name, self.type, self.init_value, self.name))

	def print_definition(self, fo, byte_pos, last, little_endian):
		fo.write("                        {\n")
		fo.write("                                {},       /* Signal ID */\n".format(self.name))


		if(little_endian):
			fo.write("(                                {})|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */\n".format(byte_pos))
		else:
			fo.write("                                {}                                       /* Byte Position */\n".format(byte_pos))

		if(last):
			fo.write("                        }\n")
		else:
			fo.write("                        },\n")


	def print_debug(self):
		print self.name
		print self.id
		print self.type
		print self.init_value
		print self.factor
		print self.offset
		print self.unit
