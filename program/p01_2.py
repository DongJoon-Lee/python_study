# p01-1-sum.py

def sum(n) :
    s = 0
    for i in range(n+1) :
        s += i
    return s

print(sum(10)) # 55
print(sum(100)) # 5050

# p01-2-sum2.py

def sum2(n) :
    return n*(n+1)//2

print(sum2(10))
print(sum2(100))


#problem

# 1-1

def sum3(n) :
    s = 0
    for i in range(n+1) :
        s += i*i
    return s

print(sum3(10))