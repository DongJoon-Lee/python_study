# p05-1-gcd.py
# 최대공약수 구하기
# 입력 : a, b
# 출력 : a와 b의 최대공약수

# def gcd(a, b) :
#     gcd = min(a, b)
#     while True :
#         if a % gcd == 0 and b % gcd == 0 :
#             return gcd
#         gcd -= 1

# print(gcd(1,5))
# print(gcd(3,6))
# print(gcd(60, 24))    
# print(gcd(81, 27))

# 유클리드 알고리즘을 통한 최대공약수 구하기
# 입력 : a, b
# 출력 : a와 b의 최대공약수

# def gcd(a, b):
#     if b == 0 :
#         return a
#     return gcd (b, a % b)

# print(gcd(1,5))
# print(gcd(3,6))
# print(gcd(60, 24))    
# print(gcd(81, 27))

# 연습문제

# 5-1
# 피보나치 수 구하기
# 입력 : n
# 출력 : 0번부터 시작, n번째 피보나치 수
# 재귀

# def fibo (n) :
#     if n == 0 :
#         return 0
#     elif n == 1 :
#         return 1
#     return fibo(n-1) + fibo(n-2)

# print(fibo(7))