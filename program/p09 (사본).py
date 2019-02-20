# # 삽입 정렬(1)

# # 들어가야 할 위치를 알려주는 함수
# # 입력 : 리스트, 들어갈 친구
# # 출력 : 들어가야할 자리

# def find_idx(a, b) :
#     n = len(a)
#     for i in range(n) :
#         if b < a[i] :
#             return i
#     return n

# # 새 리스트에 정렬하기
# # 입력 : 리스트
# # 출력 : 정렬된 새 리스트

# def isort(a) :
#     res = []
#     while a :
#         friend = a.pop(0)
#         idx = find_idx(res, friend)
#         res.insert(idx, friend)
#     return res

# d = [2,4,5,1,3]
# print(isort(d))

# # 삽입 정렬(2)
# # 입력 : 리스트 
# # 출력 : X(리스트가 정렬됨)

# def isort(a) :
#     n = len(a)
#     for i in range(1,n) :
#         friend = a[i]
#         j = i-1
#         while 0 <= j and friend < a[j] :
#             a[j+1] = a[j]
#             j -= 1
#         a[j+1] = friend

# d = [2,4,5,1,3]
# isort(d)
# print(d)

# 연습문제

# 9-1
# 삽입 정렬(2)를 통해 리스트 [2,4,5,1,3] 정렬하는 과정 적기

# i라는 기준점의 인덱스를 잡고, j를 i-1로 지정한다. 
# 만약 a[j]가 a[i]보다 크다면, a[i]보다 뒤로 가야 하므로 a[j]부터 하나씩 뒤로 민다. 
# j를 점점 줄여가면서 a[i]가 들어갈 위치를 찾는다. 
# a[i]가 더 큰 j값으로 왔을 때, j 바로 뒷자리를 a[i] 자리로 놓는다. 

# 9-2
# 내림차순 정렬로 바꾸기 위해?

# a[i]가 a[j]보다 클 때 뒤로 한 칸씩 밀어주면 된다. 
# def isort(a) :
#     n = len(a)
#     for i in range(1,n) :
#         friend = a[i]
#         j = i-1
#         while 0 <= j and a[j] < friend :
#             a[j+1] = a[j]
#             j -= 1
#         a[j+1] = friend

# d = [2,4,5,1,3]
# isort(d)
# print(d)