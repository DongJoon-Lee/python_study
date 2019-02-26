# p09-1-isort.py

def findidx(a, b) :
    n = len(a)
    for i in range(n) :
        if b < a[i] :
            return i
    return n

def isort(a) :
    res = []
    while a :
        min = a.pop(0)
        idx = findidx(res, min)
        res.insert(idx, min)
    return res

d = [2,4,5,1,3]
print(isort(d)) # [1,2,3,4,5]

# p09-2-isort.py

def isort_c(a) :
    n = len(a)
    for i in range(1, n) :
        res = a[i]
        j = i-1
        while j >= 0 and a[j] > res :
            a[j+1] = a[j]
            j -= 1
        a[j+1] = res

d = [2,4,5,1,3]
isort_c(d)
print(d)


# Problem

# 9-2

def findidx2(a, b) :
    n = len(a)
    for i in range(n) :
        if a[i] < b :
            return i
    return n

def isort2(a) :
    res = []
    while a :
        max = a.pop(0)
        idx = findidx2(res, max)
        res.insert(idx, max)
    return res

d = [2,4,5,1,3]
print(isort2(d)) # [5,4,3,2,1]

def isort2_c(a) :
    n = len(a)
    for i in range(1, n) :
        res = a[i]
        j = i-1
        while j >= 0 and a[j] < res :
            a[j+1] = a[j]
            j -= 1
        a[j+1] = res

d = [2,4,5,1,3]
isort2_c(d)
print(d)