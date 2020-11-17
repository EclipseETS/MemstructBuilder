
import os
from eclipseMemstructGen import import_memstruct_file
import dbGen


def test_integration_dbgen():
    # Open test memstruct file
    # Current test file taken 05/11/20
    board_list = import_memstruct_file("test/test_memstruct_entry.txt")

    try:
        os.mkdir("test/output")
    except OSError:
        pass

    # Generate outputs in test/output/ and open the generated file
    dbGen.generate("test/output/test_CAN_DB_E10.dbc", board_list)
    output = open("test/output/test_CAN_DB_E10.dbc")
    data = output.read()

    # Values to test with
    num_messages = 4
    num_signals = 7

    # Count the number of occurences of keywords
    assert data.count('BO_ ') == num_messages
    assert data.count('SG_ ') == num_signals
    assert data.count("VERSION") == 1
    assert data.count('NS_ :') == 1
    assert data.count('BS_:') == 1
    assert data.count('BU_:') == 1

