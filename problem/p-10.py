# 10-1

# 내림차순 정렬로 바꾸기 위해 바꿔야하는 부분.


def merge_sort(a) :
    n = len(a)

    if n <= 1 :
        return 
    
    mid = n //2
    m1 = a[:mid]
    m2 = a[mid:]
    merge_sort(m1)
    merge_sort(m2)

    i1 = 0
    i2 = 0
    m = 0

    while i1 < len(m1) and i2 < len(m2):
        if m1[i1] > m2[i2] :       # 둘의 크기를 비교하는 부분에서 더 큰 숫자를 먼저 뽑아주면 된다. 
            a[m] = m1[i1]
            m += 1
            i1 += 1
        else :
            a[m] = m2[i2]
            m += 1
            i2 += 1
    
    while i1 < len(m1) :
        a[m] = m1[i1]
        m += 1
        i1 += 1
    while i2 < len(m2) :
        a[m] = m2[i2]
        m += 1
        i2 += 1


d = [6,8,3,9,10,1,2,4,7,5]
merge_sort(d)
print(d)