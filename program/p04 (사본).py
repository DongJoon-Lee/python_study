# p04-1-fact.py
# 연속한 숫자의 곱
# 입력 : n
# 출력 : 1부터 n까지 연속한 숫자를 곱한 값

# def fact(a) :
#     sum = 1
#     for i in range(1, a+1) :
#         sum *= i
#     return sum

# print(fact(1))
# print(fact(5))
# print(fact(10))

# p04-2-fact.py
# 연속한 숫자의 곱
# 입력 : n
# 출력 : 1부터 n까지 연속한 숫자를 곱한 값
# 재귀

# def fact(a) :
#     if a <= 1 :
#         return 1
#     return a * fact(a-1)

# print(fact(1))
# print(fact(5))
# print(fact(10))

# 연습문제

# 4-1
# 문제 1의 1부터 n까지의 합 구하기를 재귀 호출로
# 입력 : n
# 출력 : 1부터 n까지의 합
# 재귀

# def sum(a) :
#     if a <= 1:
#         return 1
#     return a + sum(a-1)

# print(sum(10))
# print(sum(100))

# 4-2
# 문제 2의 숫자 n개 중 최댓값 찾기를 재귀 호출로 만들기
# 입력 : 숫자가 n개 들어있는 리스트
# 출력 : 숫자 n개 중 최대값
# 재귀

# def findmax(a) :
#     max = a.pop(0)
#     n = len(a)
#     for i in range(1, n):
#         if max < a[i] :
#             return findmax(a)
#     return max

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(findmax(v))

