# import sys  # sys module
# import os

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from program.p01 import pro1, sum1, sum2


def test_sum1():
    assert sum1(10) == 55
    assert sum1(100) == 5050

def test_sum2():
    assert sum2(10) == 55
    assert sum2(100) == 5050

def test_pro1():
    assert pro1(10) == 385