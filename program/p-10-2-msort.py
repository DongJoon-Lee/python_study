# 일반적인 병합 정렬 알고리즘
# 입력 :리스트 a
# 출력 : 없음 (a가 오름차순으로 정렬)
# 이게 더 신기함. 인덱스 3개를 따로따로 정리했음. 다시 봐야함.

def merge_sort(a) :
    n = len(a)

    if n <= 1 : # 정렬할 리스트 길이가 1 이하이면 정렬 안해도됨.
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
        if m1[i1] < m2[i2] :
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
