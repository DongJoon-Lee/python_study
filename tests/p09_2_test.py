from program.p09_2 import isort, isort2

def test_isort():
    d = [2,4,5,1,3]

    assert isort(d) == [1,2,3,4,5]

def test_isort2():
    d = [2,4,5,1,3]

    assert isort2(d) == [5,4,3,2,1]