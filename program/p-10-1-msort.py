# 쉽게 설명한 병합 정렬
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트
# 매우 똑똑하다. 다시 볼 필요가 있음. pop이 굉장히 좋은 아이이다. 

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    
    mid = n//2
    m1 = merge_sort(a[:mid])
    m2 = merge_sort(a[mid:])

    result = []
    while m1 and m2 :
        if m1[0] < m2[0]:
            result.append(m1.pop(0))
        else :
            result.append(m2.pop(0))
    while m1 :
        result.append(m1.pop(0))
    while m2 :
        result.append(m2.pop(0))
    return result

d = [6,8,3,9,10,1,2,4,7,5]
print(merge_sort(d))