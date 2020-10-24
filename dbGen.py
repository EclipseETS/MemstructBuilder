
def generate(board_list):

    with open("output/CAN_DB_E10.dbc", "w") as fo:

        final_output = (
            f'VERSION ""\n'
            f'\n'
            f'\n'
            f'NS_ : \n'
            f'\tNS_DESC_\n'
            f'\tCM_\n'
            f'\tBA_DEF_\n'
            f'\tBA_\n'
            f'\tVAL_\n'
            f'\tCAT_DEF_\n'
            f'\tCAT_\n'
            f'\tFILTER\n'
            f'\tBA_DEF_DEF_\n'
            f'\tEV_DATA_\n'
            f'\tENVVAR_DATA_\n'
            f'\tSGTYPE_\n'
            f'\tSGTYPE_VAL_\n'
            f'\tBA_DEF_SGTYPE_\n'
            f'\tBA_SGTYPE_\n'
            f'\tSIG_TYPE_REF_\n'
            f'\tVAL_TABLE_\n'
            f'\tSIG_GROUP_\n'
            f'\tSIG_VALTYPE_\n'
            f'\tSIGTYPE_VALTYPE_\n'
            f'\tBO_TX_BU_\n'
            f'\tBA_DEF_REL_\n'
            f'\tBA_REL_\n'
            f'\tBA_DEF_DEF_REL_\n'
            f'\tBU_SG_REL_\n'
            f'\tBU_EV_REL_\n'
            f'\tBU_BO_REL_\n'
            f'\tSG_MUL_VAL_\n'
            f'\n'
            f'BS_:\n'
            f'\n'
            f'BU_:\n'
            f'\n'
            '\n'
        )

        float_footer = []
        for board in board_list:
            for message in board.message:
                dlc = 0

                # Signal offset
                if board.little_endian == 1:
                    signal_offset = 0
                else:
                    signal_offset = 7

                # ID
                board_id = board.offset + message.id

                # Extended
                if board.extend == 1:
                    board_id = board_id | 0x80000000

                # DLC
                for signal in message.signal:
                    dlc = dlc + (int(signal.bitsize) / 8)

                final_output += f"BO_ {board_id} {message.name}: {dlc} Vector__XXX\n"

                for signal in message.signal:
                    # Signed
                    if signal.signed == "true":
                        signed = "-"
                    else:
                        signed = "+"
                    # Endianess
                    if board.little_endian == 1:
                        endianess = "1"
                    else:
                        endianess = "0"
                    # Float footer
                    if signal.float == "true":
                        float_footer.append(f"SIG_VALTYPE_ {board_id} {signal.name} : 1;\n")

                    final_output += f' SG_ {signal.name} : {signal_offset}|{signal.bitsize}@{endianess}{signed} ({signal.factor},{signal.offset}) [{signal.minvalue}|{signal.maxvalue}] "{signal.unit}" Vector__XXX\n'
                    signal_offset = signal_offset + int(signal.bitsize)

                final_output += f'\n'
        final_output += (
            f'\n'
            f'\n'
            f'BA_DEF_  "BusType" STRING ;\n'
            f'BA_DEF_DEF_  "BusType" "";\n'
        )
        for entry in float_footer:
            final_output += f"{entry}"
        final_output += f'\n'

        fo.write(final_output)
