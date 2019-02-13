# 숫자 n개를 리스트로 입력받아 최소값을 구하는 프로그램 만들기
# 입력: 숫자 n개로 이루어진 리스트
# 출력: 최소값

def min_num(a):
    min_num = a[0]
    length = len(a)
    for i in range(1, length):
        if a[i] < min_num:
            min_num = a[i]
    return min_num

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(min_num(v))