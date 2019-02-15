# 선택 정렬
# 입력 : 리스트 a
# 출력 : 정렬된 리스트

def min_index (a) :
    i = len(a)
    min = 0
    for x in range(1,i):
        if a[x] < a[min]:
            min = x
    return min

def sort_list (a) :
    sort = []
    i = len(a)
    for _ in range(i):  # 책에서는 while a: (리스트에 값이 남아있는 동안 계속)
        ind_num = min_index(a)
        num = a.pop(ind_num)
        sort.append(num)
    return sort

d = [2,4,5,1,3]
print(sort_list(d))
    