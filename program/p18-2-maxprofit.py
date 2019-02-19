# 다른 방식으로
# 신기함.... 어떻게 생각을 저렇게 하지
# 파는날을 중심으로
# 처음 최저값을 a[0]으로
# 둘째날부터 이익이 많이 생기면 max_profit 저장
# 최저값보다 작으면 최저값을 변경
# 한 번만 반복해서 최대 이익이 얼마인지 알 수 있음
# 입력 : 주식 가격의 변화 리스트
# 출력 : 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익

def maxprofit(a):
    max_profit = 0
    minstock = a[0]
    for i in range(1, len(a)):
        profit = a[i] - minstock
        if max_profit < profit :
            max_profit = profit
        if a[i] < minstock:
            minstock = a[i]
        
    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(maxprofit(stock))