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

	def print_callback(self):
		#fo.write(f"#ifndef {self.name}_callback\n")
		#fo.write(f"#        define {self.name}_callback NULL\n")
		#fo.write(f"#endif\n")
		return (
			f"#ifndef {self.name}_callback\n"
			f"#        define {self.name}_callback NULL\n"
			f"#endif\n"
		)

	def print_enum(self):
		return (
			f"        {self.name},\n"
		)

	def print_para_macro(self, last):
		if(last):
			#fo.write(f"        CAN_PARA_MACRO({self.name}, sizeof({self.type}), {self.init_value}, {self.name}_callback),\n\n")
			#fo.write(f"#ifdef E92_USE_CUSTOM_MEMSTRUCT\n")
			#fo.write(f"/*******************************************************************/\n")
			#fo.write(f"/*                                                    CUSTOM CAN                                                         */\n")
			#fo.write(f"/********************************************************************/\n")
			#fo.write(f"        CUSTOM_CAN_SIG,\n")
			#fo.write(f"#endif\n\n")
			return (
				f"        CAN_PARA_MACRO({self.name}, sizeof({self.type}), {self.init_value}, {self.name}_callback),\n\n"
				f"#ifdef E92_USE_CUSTOM_MEMSTRUCT\n"
				f"/*******************************************************************/\n"
				f"/*                                                    CUSTOM CAN                                                         */\n"
				f"/********************************************************************/\n"
				f"        CUSTOM_CAN_SIG,\n"
				f"#endif\n\n"
			)
		else:
			#fo.write(f"        CAN_PARA_MACRO({self.name}, sizeof({self.type}), {self.init_value}, {self.name}_callback),\n")
			return (
				f"        CAN_PARA_MACRO({self.name}, sizeof({self.type}), {self.init_value}, {self.name}_callback),\n"
			)

	def print_definition(self, byte_pos, last, little_endian):
		#fo.write(f"                        {\n")
		#fo.write(f"                                {self.name},       /* Signal ID */\n")
		str = (
			f"                        {{\n"
			f"                                {self.name},       /* Signal ID */\n"
		)
		#fo.write(str)

		if(little_endian):
			#fo.write(f"(                                {byte_pos})|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */\n")
			str += (
				f"(                                {byte_pos})|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */\n"
			)
		else:
			#fo.write(f"                                {byte_pos}                                       /* Byte Position */\n")
			str += (
				f"                                {byte_pos}                                       /* Byte Position */\n"
			)
			
		if(last):
			#fo.write(f"                        }\n")
			str += (
				f"                        }}\n"
			)
		else:
			#fo.write(f"                        },\n")
			str += (
				f"                        }},\n"
			)
		return str

	def print_definition_telemetry(self, byte_pos, last, little_endian):
		#fo.write(f"                                {\n")
        
		# Signal ID
		#fo.write(f"                                        {self.name},   /* Signal ID */\n")
		# Signal name
		#fo.write(f"                                        \"{self.name}\",   /* Signal Name */\n")
		# Signal Type (uint32_t, uint16_t, uint8_t, float, etc..)
		#fo.write(f"                                        TYPE_{self.type},   /* Signal Type */\n")
		# Byte offset of signal
		#fo.write(f"                                        {byte_pos},   /* Byte Position */\n")
		# Size of signal
		#fo.write(f"                                        sizeof({self.type}),   /* sizeof */\n")
		str = (
			f"                                {{\n"
			# Signal ID
			f"                                        {self.name},   /* Signal ID */\n"
			# Signal name
			f"                                        \"{self.name}\",   /* Signal Name */\n"
			# Signal Type (uint32_t, uint16_t, uint8_t, float, etc..)
			f"                                        TYPE_{self.type},   /* Signal Type */\n"
			# Byte offset of signal
			f"                                        {byte_pos},   /* Byte Position */\n"
			# Size of signal
			f"                                        sizeof({self.type}),   /* sizeof */\n"
		)
		#fo.write(str)
		
		# Endianess of signal
		if(little_endian):
			#fo.write(f"                                        L_ENDIAN,   /* Endianness */\n")
			str += (
				f"                                        L_ENDIAN,   /* Endianness */\n"
			)
		else:
			#fo.write(f"                                        B_ENDIAN,   /* Endianness */\n")
			str += (
				f"                                        B_ENDIAN,   /* Endianness */\n"
			)
			
		# Multiplier factor of signal
		# .x -> f, else -> .0f
		if (isinstance(self.factor, int)):
			#fo.write(f"                                        {self.factor}.0f,   /* Multiplier */\n")
			str += (
				f"                                        {self.factor}.0f,   /* Multiplier */\n"
			)
		else:
			#fo.write(f"                                        {self.factor}f,   /* Multiplier */\n")
			str += (
				f"                                        {self.factor}f,   /* Multiplier */\n"
			)
        
		if(last):
			#fo.write(f"                                }\n")
			str += (
				f"                                }}\n"
			)
		else:
			#fo.write(f"                                },\n")
			str += (
				f"                                }},\n"
			)
		return str


	def print_debug(self):
		print (self.name)
		print (self.id)
		print (self.type)
		print (self.init_value)
		print (self.factor)
		print (self.offset)
		print (self.unit)
