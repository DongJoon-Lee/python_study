# 두 번 이상 나온 이름 찾기
# 입력: 이름이 n개 들어있는 리스트
# 출력: 이름 n개중 반복되는 이름이 있는 집합

def find_same(a):
    result = set() # 집합
    n = len(a)
    for i in range(n-2): #마지막 숫자는 비교 필요 X
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same(name))
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same(name2))