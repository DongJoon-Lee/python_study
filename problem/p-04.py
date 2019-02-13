# 4-1

# 1부터 n까지의 합 구하기 (재귀)
# 입력: n
# 출력: 1부터 n까지의 합

def sum_re(a):
    if a <= 1:
        return a;
    return a + sum_re(a-1)


print(sum_re(10))


# 4-2

# 숫자 n개 중 최댓값 찾기 (재귀)
# 입력: 숫자 n개로 이루어진 리스트
# 출력: 최댓값

def max(a):
    m = a.pop(0)
    l = len(a)
    for i in range(l):
        if m < a[i]:
            return max(a)
    return m

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(max(v))