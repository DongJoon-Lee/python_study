# 리스트 내에서 최대값의 위치번호 구하기
# 입력: 숫자 n개가 있는 리스트
# 출력: 숫자 n개중 최대값의 위치번호

def max_n(a):
    max_n=0
    n = len(a)
    for i in range(1,n):
        if a[i] > a[max_n]:
            max_n= i
    return max_n

v = [17,92, 18, 33, 58, 7, 33, 42]

print(max_n(v))