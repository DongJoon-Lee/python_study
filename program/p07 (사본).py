# 리스트에서 특정 숫자의 위치 찾기
# 입력 : 리스트 a, 찾는 값
# 출력 : 특정 숫자의 위치

# def search_list(a, b) :
#     n = len(a)
#     for i in range(n) :
#         if b == a[i] :
#             return i
#     return -1

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(search_list(v, 18))
# print(search_list(v, 33))
# print(search_list(v, 900))

# -> 계산 복잡도는 최악의 경우를 계산했을 때 O(n)

# 연습문제

# 7-1
# 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 알고리즘
# 찾는 값이 없으면 빈 리스트 return
# 입력 : 리스트 a, 찾는 값
# 출력 : 특정 숫자의 위치의 리스트

# def search_list_all(a, b) :
#     n = len(a)
#     res = []
#     for i in range(n) :
#         if b == a[i] :
#             res.append(i)
#     return res

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(search_list_all(v, 18))
# print(search_list_all(v, 33))
# print(search_list_all(v, 900))

# 7-2
# 연습문제 7-1의 계산 복잡도는?
# O(n)이다. 만약 앞에서 같은 숫자를 찾아도, 리스트에 추가하고 끝까지 찾아봐야 하기 때문에, 어차피 n번의 계산을 해야한다. 

# 7-3
# 학생 번호와 이름이 리스트로 주어졌을 때 학생 번호를 입력하면 번호에 해당하는 이름을 돌려주는 함수. 없으면 ?
# 입력 : 학생 번호 리스트, 학생 이름 리스트, 학생 번호
# 출력 : 학생 이름

# def find_stu(a, b, c) :
#     n = len(a)
#     for i in range(n) :
#         if c == a[i] :
#             return b[i]
#     return '?'

# stu_no = [39, 14, 67, 105]
# stu_name = ["Justin", "John", "Mike", "Summer"]

# print(find_stu(stu_no, stu_name, 67))
# print(find_stu(stu_no, stu_name, 101))