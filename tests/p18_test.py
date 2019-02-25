from program.p18 import maxprofit, maxprofit2

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

def test_maxprofit():
    assert maxprofit(stock) == 2400

def test_maxprofit2():
    assert maxprofit2(stock) == 2400