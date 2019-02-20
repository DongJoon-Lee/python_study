from program.p05 import gcd, gcd2, fibo

def test_gcd():
    assert gcd(1,5) == 1
    assert gcd(3,6) == 3
    assert gcd(60, 24) == 12
    assert gcd(81, 27) == 27

def test_gcd2():
    assert gcd2(1,5) == 1
    assert gcd2(3,6) == 3
    assert gcd2(60, 24) == 12
    assert gcd2(81, 27) == 27

def test_fibo():
    assert fibo(7) == 13