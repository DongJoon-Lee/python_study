# 집합 정리

# set()
# - 빈 집합 만들기
# len(s)
# - 집합의 길이를 구함
# add(x)
# - 집합에 자료 x를 추가함
# discard(x)
# - 집합에 자료 x가 있으면 삭제함(없으면 변화 X)
# clear()
# - 집합의 모든 자료를 지움
# x in s
# - 어떤 자료 x가 집합 s에 있는지 확인 (x not in s 는 없는지 확인)

# p03-1-samename.py
# 두 번 이상 나온 이름 찾기
# 입력 : 이름이 n개 있는 리스트
# 출력 : 이름 n개중 반복되는 이름의 집합

# def samename(a) :
#     n = len(a)
#     res = set()
#     for i in range (n-1) :
#         for j in range(i+1, n) :
#             if a[i] == a[j] :
#                 res.add(a[i])
#     return res

# name = ["Tom", "Jerry", "Mike", "Tom"]
# print(samename(name))
# name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
# print(samename(name))

# 연습문제

# 3-1
# n명중 두 명 뽑을 때, 짝을 지을 수 있는 모든 조합 출력하기
# 입력 : 이름이 n개 있는 리스트
# 출력 : 두 명을 뽑을 때, 짝을 지을 수 있는 모든 조합

# def pro31(a) :
#     n = len(a)
#     for i in range(n-1) :
#         for j in range(i+1, n) :
#             print(a[i], '-', a[j])

# v = ["Tom", "Jerry", "Mike"]
# pro31(v)

# 3-2
# 대문자 O 표기법으로 표현하기

# A : 65536
# O(1) -> 계산 횟수가 고정되어있음
# B : n - 1
# O(n) -> 계산 횟수가 n에 비례
# C : 2n^2/3 + 10000n
# O(n^2) -> 계산 횟수가 n의 제곱에 비례해서 계산 시간이 변함, 앞의 2/3 무시.
# D : 3n^4 - 4n^3 + 5n^2 -6n + 7
# O(n^4) -> 계산 횟수가 n의 네제곱에 비례해서 계산 시간이 변함, 앞의 3 무시.
