# p04-1-fact.py

def fact(a) :
    s = 1
    for i in range(1, a+1) :
        s *= i
    return s

print(fact(1)) # 1
print(fact(5)) # 120
print(fact(10)) # 3628800

# p04-2-fact.py

def fact2(a) :
    if a <= 1 :
        return 1
    return a * fact2(a-1)

print(fact2(1))
print(fact2(5))
print(fact2(10))


# Problem

# 4-1

def sum(a) :
    if a <= 1 :
        return 1
    return a + sum(a-1)

print(sum(10))
print(sum(100))

# 4-2

def findmax(a) :
    max = a.pop(0)
    n = len(a)
    for i in range(n) :
        if max < a[i] :
            return findmax(a)
    return max

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(findmax(v)) # 92