from program.p11_2 import qsort, bsort

def test_qsort():
    d = [6,8,3,9,10,1,2,4,7,5]
    assert qsort(d) == [1,2,3,4,5,6,7,8,9,10]

def test_bsort():
    d = [6,8,3,9,10,1,2,4,7,5]
    assert bsort(d) == [1,2,3,4,5,6,7,8,9,10]