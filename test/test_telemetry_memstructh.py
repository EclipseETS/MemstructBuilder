

import re
import os
from eclipseMemstructGen import import_memstruct_file
import telemetryMemstructh


def test_telemetry_memstructh():
    # Open test memstruct file
    # Current test file taken 05/11/20
    board_list = import_memstruct_file("test/test_memstruct_entry.txt")

    try:
        os.mkdir("test/output")
    except OSError:
        pass

    # Generate outputs in test/output/ and open the generated file
    telemetryMemstructh.generate("test/output/test_telemetry_memstruct.h", board_list)
    output = open("test/output/test_telemetry_memstruct.h")
    data = output.read()

    num_boards = 3
    num_messages = 4
    num_signals = 7

    # Test header guards are present
    assert data.count('#ifndef TELEMETRY_MEMSTRUCT_H_\n'
                      '#define TELEMETRY_MEMSTRUCT_H_') == 1

    # Test CAN definitions are present
    assert data.count('#define CANFRM_EXTENDED_ID  (1<<29)\n'
                      '#define CANFRM_RTR          (1<<30)') == 1

    # Definitions for big and little endian
    assert data.count('#define L_ENDIAN') == 1
    assert data.count('#define B_ENDIAN 1') == 1

    # Test that DATA_TYPE definition is present
    assert data.count('enum DATA_TYPE') == 1

    # Test board enum
    assert data.count('ID_OFFSET_DRIVER = 0x100,') == 1
    assert data.count('ID_OFFSET_BMS = 0x300L | CANFRM_EXTENDED_ID,') == 1
    assert data.count('ID_OFFSET_DASHBOARD = 0x400L | CANFRM_EXTENDED_ID') == 1

    # Test enums and struct are present
    assert data.count('enum CAN_ID') == 1
    assert data.count('enum SIGNAL_ID') == 1
    assert data.count('struct SignalDecode') == 1
    assert data.count('struct MessageDecode') == 1

    # Test can message definitions are present
    assert sum(1 for m in re.finditer('static constexpr .+ CAN_MESSAGES', data)) == 1

    # Test number of occurences of message and signal definitions
    assert sum(1 for m in re.finditer(' M_[A-Z_]+,', data)) + \
           sum(1 for m in re.finditer(' M_[A-Z_]+ = ', data)) == num_messages * 3
    assert sum(1 for m in re.finditer(' S_[A-Z_]+,', data)) == num_signals * 2



