# 버블정렬!
# 입력 : 리스트 a
# 출력 : X (a가 정렬됨)

def bsort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j+1] < a[j]:
                a[j+1], a[j] = a[j], a[j+1]
    
d = [2,4,5,1,3]
bsort(d)
print(d)


# sorted([5,2,3,1,4]) => 새로운 리스트를 만들어줌
# a = [5,2,3,1,4]
# a.sort() => 그냥 a를 정렬