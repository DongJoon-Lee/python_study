# # 선택 정렬(1)

# # 최솟값 찾기
# # 입력 : 리스트 a
# # 출력 : 가장 작은 값

# def find_min_idx(a) :
#     min_idx = 0
#     n = len(a)
#     for i in range(n) :
#         if a[i] < a[min_idx] :
#             min_idx = i
#     return min_idx

# # 새 리스트에 정렬하기
# # 입력 : 리스트 a
# # 출력 : 오름차순으로 정렬된 새 리스트

# def ssort(a) :
#     res = []
#     while a :
#         min_idx = find_min_idx(a)
#         min = a.pop(min_idx)
#         res.append(min)
#     return res

# d = [2,4,5,1,3]
# print(ssort(d))

# # 선택 정렬(2)
# # 입력 : 리스트 a
# # 출력 : X(리스트 a가 오름차순으로 정렬)

# def ssort(a) :
#     n = len(a)
#     for i in range(n-1) :
#         min_idx = i
#         for j in range(i+1, n) :
#             if a[j] < a[min_idx] :
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]

# d = [2,4,5,1,3]
# ssort(d)
# print(d)

# 연습문제

# 8-1
# 선택 정렬(2)를 사용해 리스트 [2,4,5,1,3]을 정렬하는 과정 적기

# 처음으로, 인덱스 0번을 min idx로 놓는다. 
# 그 다음 인덱스 0번의 값인 2를 비교하여 더 작은 친구가 있는지 보고, 있다면 그 친구를 min idx로 놓는다. 
# 0번과 그 min dex의 값을 바꿔준다. 
# 그 행위를 0 ~ 3번까지 반복한다. 

# 8-2
# 오름차순 정렬을 내림차순 정렬로 바꾸기 위해 바꿔야 하는 부분. (선택 정렬(2) 사용)

# 내림차순 정렬로 바꾸기 위해서는 가장 큰 값이 앞으로 오면 된다. 

# def ssort(a) :
#     n = len(a)
#     for i in range(n-1) :
#         max_idx = i
#         for j in range(i+1, n) :
#             if a[max_idx] < a[j] :
#                 max_idx = j
#         a[i], a[max_idx] = a[max_idx], a[i]

# d = [2,4,5,1,3]
# ssort(d)
# print(d)

# 이렇게 바꾸면 된다. 