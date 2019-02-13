# 3-1

# n명 중 두 명을 뽑아 지을 수 있는 짝을 출력하는 알고리즘
# 입력 : 이름 리스트
# 출력 : 짝을 지을 수 있는 모든 경우

def jjak(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            print(a[i],"-",a[j])
            print()

v = ["Tom", "Jerry", "Mike"]

print(jjak(v))

# 3-2

# 대문자 O 표기법으로 표현

# 65536
# O(1)

# n-1
# O(n)

# 2n^2/3 + 10000n
# O(n^2) 

# 3n^4 - 4n^3 + 5n^2 - 6n + 7
# O(n^4)