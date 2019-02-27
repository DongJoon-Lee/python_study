from program.p17_2 import find_fake,find_fake2

def test_find_fake():
    n = 100
    assert find_fake(0, 100) == 29

def test_find_fake2():
    n = 100
    assert find_fake2(0, 100) == 29