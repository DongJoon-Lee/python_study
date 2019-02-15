# 최대공약수 구하기 (재귀)
# 입력: a, b
# 출력: a와 b의 최대공약수
# 더 신기함.

def findgcd(a,b):
    if b == 0 :
        return a
    return findgcd(b,a%b)

print(findgcd(1,5))
print(findgcd(3,6))
print(findgcd(60,24))
print(findgcd(81,27))