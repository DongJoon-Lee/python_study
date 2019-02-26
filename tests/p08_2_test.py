from program.p08_2 import ssort, ssort2

def test_ssort():
    d = [2,4,5,1,3]

    assert ssort(d) == [1,2,3,4,5]

def test_ssort2():
    d = [2,4,5,1,3]

    assert ssort2(d) == [5,4,3,2,1]