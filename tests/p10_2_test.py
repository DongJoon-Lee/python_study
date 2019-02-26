from program.p10_2 import msort, msort2

def test_msort():
    d = [6,8,3,9,10,1,2,4,7,5]
    assert msort(d) == [1,2,3,4,5,6,7,8,9,10]

def test_msort2():
    d = [6,8,3,9,10,1,2,4,7,5]
    assert msort2(d) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
