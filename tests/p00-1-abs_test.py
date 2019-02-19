import sys  # sys module
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from program.p00_1_abs import abs_sign
def test_abs_sign():
    assert abs_sign(-1) == 1