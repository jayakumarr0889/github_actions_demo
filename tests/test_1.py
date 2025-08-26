import os, sys

sys.path.insert(0, os.getcwd())

from script import addition

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

    # Test with large numbers
    assert addition(1000000, 2000000) == 3000000
