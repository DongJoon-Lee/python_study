# 가짜 동전 찾기
# 예시에서는 29번 동전이 가짜인걸로 설정
# 입력 : 동전 시작과 끝
# 출력 : 가짜 동전의 위치번호

# a에서 b까지 놓인 동전을 왼쪽에 올리고
# c에서 d까지 놓인 동전을 오른쪽에 올림
# 왼쪽이 가벼우면 -1
# 오른쪽이 가벼우면 1
# 둘이 같으면 0

def weigh(a,b,c,d):
    fake_coin = 29
    if a<= fake_coin and fake_coin <= b :
        return -1
    if c <= fake_coin and fake_coin <= d :
        return 1
    return 0

def find_fake(a,b) :
    for i in range(a+1, b+1):
        res = weigh(a,a,i,i)
        if res == -1:
            return left
        elif res == 1:
            return i
    return -1 # 예외

n = 100
print(find_fake(0, n))