from program.p18_2 import max_profit, max_profit2

def test_max_profit():
    stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
    assert max_profit(stock) == 2400

def test_max_profit2():
    stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
    assert max_profit2(stock) == 2400