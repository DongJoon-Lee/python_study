from program.p17 import find_fake, find_fake2

n = 100

def test_find_fake():
    assert find_fake(0,n) == 29

def test_find_fake2():
    assert find_fake2(0,n) == 29