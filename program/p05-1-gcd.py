# 최대공약수 구하기(예시)
# 입력 : a, b
# 출력 : a, b의 최대공약수
# 신기...

def findgcd(a, b):
    i = min(a, b) # 두 수 중 더 작은 값을 저장
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1

print(findgcd(1,5))
print(findgcd(3,6))
print(findgcd(60, 24))
print(findgcd(81, 27))