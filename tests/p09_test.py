from program.p09 import isort

def test_isort():
    d = [2,4,5,1,3]
    assert isort(d) == [1,2,3,4,5]