# 하노이탑 (재귀)
# 입력 : 원반 개수, 원반 시작점, 원반 도착점, 보조점?
# 출력 : 원반 이동 순서

def hanoi(n,from_,to,sub):
    if n == 1:
        print(from_,"->",to)
        return

    hanoi(n-1,from_,sub,to)
    print(from_,"->",to)
    hanoi(n-1,sub,to,from_)


print("n=1")
print(hanoi(1,1,3,2))
print("n=2")
print(hanoi(2,1,3,2))
print("n=3")
print(hanoi(3,1,3,2))