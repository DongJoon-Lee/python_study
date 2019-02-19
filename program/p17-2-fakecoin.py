# 가짜 동전 찾기 (이분 탐색)

def weigh(a,b,c,d):
    fake_coin = 29
    if a<= fake_coin and fake_coin <= b :
        return -1
    if c <= fake_coin and fake_coin <= d :
        return 1
    return 0
#이건 공통

# 재귀 잘 못쓰는데 쓰다보니 신기함!
def find_fake(a, b):
    if a == b :
        return a # 시작점과 끝 점이 같으면 그게 가짜 동전
    
    m = (a + b)//2
    left1 = a
    right1 = m-1
    left2 = m+1
    right2 = b
    res = weigh(left1, right1, left2, right2)
    if res == -1 :
        return find_fake(left1, right1)
    elif res == 1:
        return find_fake(left2, right2)
    return m

n = 100
print(find_fake(0,n))