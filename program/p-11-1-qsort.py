# 쉽게 설명한 퀵 정렬
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

def quick_sort(a):
    n = len(a)
    if n <= 1 :
        return a
    
    pivot = a[-1] # 기준 정하기, 편의상 마지막걸로
    m1 = []
    m2 = []
    for i in range (n-1) :
        if a[i] < pivot:
            m1.append(a[i])
        else :
            m2.append(a[i])
    return quick_sort(m1) + [pivot] + quick_sort(m2)


d = [6,8,3,9,10,1,2,4,7,5]
print(quick_sort(d))