# p18-1-maxprofit.py

def max_profit(a) :
    n = len(a)
    maxprofit = 0
    for i in range(n-1) :
        for j in range(i+1,n) :
            profit = a[j] - a[i]
            if maxprofit < profit :
                maxprofit = profit
    return maxprofit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))

# p18-2-maxprofit.py

def max_profit2(a) :
    n = len(a)
    maxprofit = 0
    min = a[0]
    for i in range(1, n) :
        if maxprofit < (a[i] - min) :
            maxprofit =  a[i] - min
        if a[i] < min :
            min = a[i]
    return maxprofit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit2(stock))