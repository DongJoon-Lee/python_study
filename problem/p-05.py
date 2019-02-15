# 5-1

# 피보나치 수열 (재귀)
# 입력 : a
# 출력 : a번째 피보나치 수 (0번으로 시작)


def fibo(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    return fibo(a-1) + fibo(a-2)


print(fibo(7))
print(fibo(4))