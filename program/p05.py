# p05-1-gcd.py

def gcd(a, b) :
    gcd = min(a, b)
    while True :
        if a % gcd == 0 and b % gcd == 0 :
            return gcd
        gcd -= 1

print(gcd(1,5)) # 1
print(gcd(3,6)) # 3
print(gcd(60, 24)) # 12   
print(gcd(81, 27)) # 27


def gcd2(a, b):
    if b == 0 :
        return a
    return gcd2(b, a % b)

print(gcd2(1,5)) # 1
print(gcd2(3,6)) # 3
print(gcd2(60, 24)) # 12   
print(gcd2(81, 27)) # 27

# Problem

# 5-1

def fibo (n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(7)) # 13