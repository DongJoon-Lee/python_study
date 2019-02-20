# # 병합 정렬(1)
# # 입력 : 리스트 
# # 출력 : 정렬된 새 리스트

# def msort(a) :
#     n = len(a)

#     if n <= 1 :
#         return a
    
#     m = n//2
#     a1 = msort(a[:m])
#     a2 = msort(a[m:])
#     res = []

#     while a1 and a2 :
#         if a1[0] < a2[0] :
#             res.append(a1.pop(0))
#         else :
#             res.append(a2.pop(0))
#     while a1 :
#         res.append(a1.pop(0))
#     while a2 :
#         res.append(a2.pop(0))
    
#     return res

# d = [6,8,3,9,10,1,2,4,7,5]
# print(msort(d))

# # 병합 정렬(2)
# # 입력 : 리스트
# # 출력 : 정렬된 새 리스트
# # 재귀

# def msort(a) :
   
#     n = len(a)

#     if n <= 1 :
#         return

#     m = n//2
#     a1 = a[:m]
#     a2 = a[m:]
#     msort(a1)
#     msort(a2)

#     n1 = 0
#     n2 = 0
#     na = 0
#     while n1 < len(a1) and n2 < len(a2) :
#         if a1[n1] < a2[n2] :
#             a[na] = a1[n1]
#             na += 1
#             n1 += 1
#         else :
#             a[na] = a2[n2]
#             na += 1
#             n2 += 1
#     while n1 < len(a1) :
#         a[na] = a1[n1]
#         na += 1
#         n1 += 1
#     while n2 < len(a2) :
#         a[na] = a2[n2]
#         na += 1
#         n2 += 1

# d = [6,8,3,9,10,1,2,4,7,5]
# msort(d)
# print(d)

# # 연습문제

# # 10-1
# # 병합 정렬(2)를 내림차순으로 바꾸기 위해서는?
# # 두 수를 비교하는 부분에서 더 큰 숫자가 들어가게 하면 된다. 
# def msort(a) :
   
#     n = len(a)

#     if n <= 1 :
#         return

#     m = n//2
#     a1 = a[:m]
#     a2 = a[m:]
#     msort(a1)
#     msort(a2)

#     n1 = 0
#     n2 = 0
#     na = 0
#     while n1 < len(a1) and n2 < len(a2) :
#         if a2[n2] < a1[n1] :
#             a[na] = a1[n1]
#             na += 1
#             n1 += 1
#         else :
#             a[na] = a2[n2]
#             na += 1
#             n2 += 1
#     while n1 < len(a1) :
#         a[na] = a1[n1]
#         na += 1
#         n1 += 1
#     while n2 < len(a2) :
#         a[na] = a2[n2]
#         na += 1
#         n2 += 1

# d = [6,8,3,9,10,1,2,4,7,5]
# msort(d)
# print(d)