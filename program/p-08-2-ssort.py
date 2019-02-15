# 선택 정렬
# 입력 : 리스트 a
# 출력 : X (리스트 a가 오름차순으로 정렬됨)



def ssort(a):
    i = len(a)
    for x in range(i-1):
        min_index = x
        for y in range(x+1,i):
            if a[y] < a[min_index]:
                min_index = y # min_index를 더 작은게 나올 때마다 바꿔주고
        a[x],a[min_index] = a[min_index],a[x]  # 그거랑 x의 값을 바꿔준다. 
# 조금 어려웠다



d = [2,4,5,1,3]
print(ssort(d))
print(d)