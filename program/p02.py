# 리스트 정리

# len(a)
# - 리스트 길이를 구함
# append(x)
# - 자료 x를 리스트 맨 뒤에 추가함
# insert(i, x)
# - 리스트의 i번 위치에 x를 추가함, 원래 있던 친구들은 하나씩 뒤로 미룸
# pop(i)
# - i번 위치에 있던 자료를 리스트에서 빼고, 그 값을 함수의 결과값으로 return함. i가 없으면 가장 마지막 값을 줌
# clear()
# - 리스트 모든 자료를 지움
# x in a
# - 자료 x가 리스트 a 안에 있는지 확인함 (x not in a는 없는지 확인)

# p02-1-findmax.py

# 최댓값 구하기
# 입력 : 숫자가 n개 들어있는 리스트
# 출력 : 숫자 n개 중 최대값

# def findmax(a) :
#     max = a[0]
#     n = len(a)
#     for i in range(1, n):
#         if max < a[i] :
#             max = a[i]
#     return max

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(findmax(v))

# p02-2-findmaxidx.py

# 최댓값의 위치 구하기
# 입력 : 숫자가 n개 들어있는 리스트
# 출력 : 숫자 n개 중 최댓값의 위치

# def findmaxidx(a) :
#     maxidx = 0
#     n = len(a)
#     for i in range(1, n) :
#         if a[maxidx] < a[i] :
#             maxidx = i
#     return maxidx

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(findmaxidx(v))

# 연습문제

# 2-1
# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램 만들기
# 입력 : 숫자 n개가 들어있는 리스트
# 출력 : 숫자 n개중 최솟값

# def findmin(a) :
#     min = a[0]
#     n = len(a)
#     for i in range(1, n) :
#         if a[i] < min :
#             min = a[i]
#     return min

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(findmin(v))