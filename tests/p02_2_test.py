from program.p02_2 import findmax, findmaxidx, findmin

v = [17, 92, 18, 33, 58, 7, 33, 42]

def test_findmax():
    assert findmax(v) == 92

def test_findmaxidx():
    assert findmaxidx(v) == 1

def test_findmin():
    assert findmin(v) == 7