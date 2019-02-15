# 삽입 정렬
# 입력 : 리스트 a
# 출력 : X (리스트 a가 오름차순으로 정렬)

# 방법 : 교체
def isort(a) :
    i = len(a)
    for x in range(1,i):
        key = a[x]
        j = x-1
        while j >= 0 and a[j] > key : # ?
            a[j +1] = a[j]
            j -= 1
            a[j+1] = key # 하나씩 옆으로 밀어줌,, 어렵다 똑똑하구만
            

v = [2,4,5,1,3]
isort(v)
print(v)