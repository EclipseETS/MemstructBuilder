
import re
import os
from eclipseMemstructGen import import_memstruct_file
import memstructc


def test_integration_memstructc():
    # Open test memstruct file
    # Current test file taken 05/11/20
    board_list = import_memstruct_file("test/test_memstruct_entry.txt")

    try:
        os.mkdir("test/output")
    except OSError:
        pass

    # Generate outputs in test/output/ and open the generated file
    memstructc.generate("test/output/test_memstruct.c", board_list)
    output = open("test/output/test_memstruct.c")
    data = output.read()

    num_boards = 3
    num_messages = 4
    num_signals = 7

    # Verify that the CAN_PARA_MACRO is defined in the same way
    assert data.count('#define CAN_PARA_MACRO(signame, width, initValue, callback) { CANSIG_UNCHANGED, '
                      'width, initValue, callback }') == 1

    # Test number of macro definitions (1 macro per signal)
    assert data.count('        CAN_PARA_MACRO(') == num_signals
    # Test number of TXRX defines (1 per board)
    assert sum(1 for m in re.finditer('#        define M_[A-Z_]+_TXRX CANMSG_RX', data)) == num_boards
    # Test the signal definition array
    assert data.count('const CANMSG_PARA CanMsg[CANMSG_N] = {') == 1

    # Changing comments in array will break unit-test, but this is
    # a cheap and reliable way of counting the definitions
    assert data.count('/* CAN-Identifier */') == num_messages + 1  # (Accounting for custom CAN)
    assert data.count('/* Signal ID */') == num_signals

    # Test CUSTOM_CAN definition is present once
    assert data.count('CUSTOM_CAN_MSG') == 1
