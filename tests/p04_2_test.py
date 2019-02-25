from program.p04_2 import fact, fact2, sum


def test_fact():
    assert fact(1) == 1
    assert fact(5) == 120
    assert fact(10) == 3628800

def test_fact2():
    assert fact2(1) == 1
    assert fact2(5) == 120
    assert fact2(10) == 3628800