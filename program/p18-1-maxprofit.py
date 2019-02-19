# 입력 : 주식 가격의 변화 리스트
# 출력 : 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익

def maxprofit(a) :
    max_profit = 0
    n = len(a)
    for i in range(n-1):
        for j in range(i,n):
            profit = a[j] - a[i]
            if max_profit < profit :
                max_profit = profit
    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(maxprofit(stock))