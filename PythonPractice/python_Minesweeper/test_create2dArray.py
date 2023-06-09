from create2dArray import *

def test_heightOf2dArray():
    listHeight = len(create2dArray(5,5))
    assert listHeight == 5, "value should be 5"

def test_widthOf2dArray():
    listWidth = len(create2dArray(5,6)[0])
    assert listWidth == 6, "value should be 6"