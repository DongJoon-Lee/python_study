# 리스트에서 특정 숫자의 위치 찾기
# 입력 : 리스트 a, 찾는 값 b
# 출력 : 찾으면 위치, 못찾으면 -1

def search(a, b):
    i = len(a)
    for x in range (i):
        if b == a[x]:
            return x
    return -1

v = [17,92,18,33,58,7,33,42]
print(search(v,18))
print(search(v,33))
print(search(v,900))