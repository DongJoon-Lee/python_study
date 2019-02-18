# 이분탐색
# 입력 : 리스트 a, 찾는값 x
# 출력 : x가 있는 위치, 없으면 -1

def bsearch(a, x):
    start = 0
    end = len(a)-1
    while start <= end:
        m = (start+end)//2
        if a[m] == x:
            return m
        elif x < a[m]:
            end = m-1
        else :
            start = m+1
    return -1

d = [1,4,9,16,25,36,49,64,81]
print(bsearch(d,36))
print(bsearch(d,50))
