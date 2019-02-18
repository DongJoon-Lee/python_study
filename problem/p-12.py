# 재귀호출을 이용한 이분 탐색 알고리즘 만들기
# 입력 : 리스트 a, 찾는 값 x
# 출력 : 찾는 값의 위치, 없으면 -1

# def bsearch(a, x):
#     # 종료 조건
#     if len(a) == 0 :
#         return -1
    
#     # 시작
#     m = len(a)//2
#     if x == a[m] :
#         return m
#     elif x < a[m]:
#         bsearch(a[:m],x)
#     else :
#         bsearch(a[m+1:],x)

# d = [1,4,9,16,25,36,49,64,81] #len(d) == 9
# print(bsearch(d,36))
# print(bsearch(d,50))

#결과가 모두 None으로 나옴, 다시 시작
# return을 안썼음... 멍청

# def bsearch(a, x):
#     if len(a) == 0:
#         return -1

#     m = len(a)//2
#     if x == a[m]:
#         return m
#     elif x < a[m]:
#         return bsearch(a[:m], x)
#     else :
#         print(m)
#         return m + bsearch(a[m+1:], x)

# d = [1,4,9,16,25,36,49,64,81] #len(d) == 9
# #print(bsearch(d,36))
# print(bsearch(d,50))

# 1번값이 0으로 나옴, 자른 다음에 인덱스를 반영 안함. 
# qsort처럼 시작 끝 값을 정해주면 가능함(자르지 않고 전체를 계속 넣으면)

def bsearch_(a, x, start, end):
    if end < start:
        return -1
    
    m = (start+end)//2
    if a[m] == x:
        return m
    elif a[m] < x :
        return bsearch_(a, x, m+1, end)
    else :
        return bsearch_(a, x, start, m-1)
    
    return -1
        
def bsearch(a, x):
    return bsearch_(a, x, 0, len(a)-1)

d = [1,4,9,16,25,36,49,64,81] #len(d) == 9
print(bsearch(d,36))
print(bsearch(d,50))