from program.p04 import fact, fact2, sum, findmax

def test_fact():
    assert fact(1) == 1
    assert fact(5) == 120
    assert fact(10) == 3628800

def test_fact2():
    assert fact2(1) == 1
    assert fact2(5) == 120
    assert fact2(10) == 3628800

def test_sum():
    assert sum(10) == 55
    assert sum(100) == 5050

def test_findmax():
    v = [17, 92, 18, 33, 58, 7, 33, 42]
    assert findmax(v) == 92