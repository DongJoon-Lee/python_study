from program.p01_2 import sum3, sum, sum2


def test_sum():
    assert sum(10) == 55
    assert sum(100) == 5050

def test_sum2():
    assert sum2(10) == 55
    assert sum2(100) == 5050

def test_sum3():
    assert sum3(10) == 385