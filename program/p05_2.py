# p05-1-gcd.py

def gcd(a,b) :
    i = min(a,b)
    while True :
        if a % i == 0 and b % i == 0 :
            return i
        i -= 1
        
print(gcd(1,5)) # 1
print(gcd(3,6)) # 3
print(gcd(60, 24)) # 12
print(gcd(81, 27)) # 27

# p05-2-gcd.py

def gcd2(a, b) :
    if b == 0 :
        return a
    return gcd2(b, a % b)

print(gcd2(1,5)) # 1
print(gcd2(3,6)) # 3
print(gcd2(60, 24)) # 12
print(gcd2(81, 27)) # 27


# Problem

# 5-1

def fibo(a) :
    if a <= 1 :
        return a
    return fibo(a-1) + fibo(a-2)

print(fibo(7))