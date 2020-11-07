
import re
import os
from eclipseMemstructGen import import_memstruct_file
import memstructh


def test_integration_memstructc():
    # Open test memstruct file
    # Current test file taken 05/11/20
    board_list = import_memstruct_file("test/test_memstruct_entry.txt")

    try:
        os.mkdir("test/output")
    except OSError:
        pass

    # Generate outputs in test/output/ and open the generated file
    memstructh.generate("test/output/test_memstruct.h", board_list)
    output = open("test/output/test_memstruct.h")
    data = output.read()

    num_boards = 3
    num_messages = 4
    num_signals = 7

    # Test header guards are present
    assert data.count('#ifndef MEMSTRUCT_H_\n'
                      '#define MEMSTRUCT_H_') == 1
    # Test necessary headers
    assert data.count('#include <stddef.h>') == 1
    assert data.count('#include "can_cfg.h"') == 1
    assert data.count('#include "can_sig.h"') == 1
    assert data.count('#include "can_msg.h"') == 1
    assert data.count('#include "can_frm.h"') == 1
    assert data.count('#include "service_can_callbacks.h"') == 1

    # Test CAN definitions are present
    assert data.count('#define CANFRM_EXTENDED_ID  (1<<29)\n'
                      '#define CANFRM_RTR          (1<<30)') == 1

    # Test number of callback definitions
    assert sum(1 for m in re.finditer('define S_[A-Z_]+_callback NULL', data)) == num_signals

    # Test board enum
    assert data.count('ID_OFFSET_DRIVER = 0x100,') == 1
    assert data.count('ID_OFFSET_BMS = 0x300L | CANFRM_EXTENDED_ID,') == 1
    assert data.count('ID_OFFSET_DASHBOARD = 0x400L | CANFRM_EXTENDED_ID') == 1

    # Test signal definitions
    assert sum(1 for m in re.finditer('S_[A-Z_]+,', data)) == num_signals + 1  # (Accounting for S_CUSTOM_SIGNALS_ID)

    # Test message definitions
    assert sum(1 for m in re.finditer('M_[A-Z_]+,', data)) + \
           sum(1 for m in re.finditer('M_[A-Z_]+ = .,', data)) == num_messages + num_boards
