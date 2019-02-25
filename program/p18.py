# p18-1-maxprofit.py

def maxprofit(a) :
    profit = 0
    n = len(a)
    for i in range(n-1) :
        for j in range(i+1, n) :
            if profit < a[j] - a[i] :
                profit = a[j] - a[i]
    return profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(maxprofit(stock))

# p18-2-maxprofit.py

def maxprofit2(a) :
    profit = 0
    minidx = 0
    n = len(a)
    for i in range(1, n) :
        if a[i] < a[minidx] :
            minidx = i
        if profit < a[i] - a[minidx] :
            profit = a[i] - a[minidx]
    return profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(maxprofit2(stock))