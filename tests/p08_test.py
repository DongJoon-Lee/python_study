from program.p08 import ssort

def test_ssort():
    d = [2,4,5,1,3]
    assert ssort(d) == [1,2,3,4,5]