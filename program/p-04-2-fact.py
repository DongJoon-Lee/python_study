# 연속한 숫자의 곱을 구하는 알고리즘(재귀 사용)
# 입력: n
# 출력: 1부터 n까지의 연속한 숫자들을 곱한 값

def fact2(a):
    if a <= 1:
        return 1
    return a * fact2(a-1)

print(fact2(1))
print(fact2(5))
print(fact2(10))