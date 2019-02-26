from program.p12_2 import bsearch, bsearch2

def test_bsearch():
    d = [1,4,9,16,25,36,49,64,81]
    assert bsearch(d, 36) == 5
    assert bsearch(d, 50) == -1

def test_bsearch2():
    d = [1,4,9,16,25,36,49,64,81]
    assert bsearch2(d, 36) == 5
    assert bsearch2(d, 50) == -1