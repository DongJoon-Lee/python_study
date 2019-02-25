# p02-1-findmax.py

def findmax(a) :
    max = a[0]
    n = len(a)
    for i in range(1, n) :
        if max < a[i] :
            max = a[i]
    return max

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(findmax(v)) # 92

# p02-2-findmaxidx.py

def findmaxidx(a) :
    maxidx = 0
    n = len(a)
    for i in range(1, n) :
        if a[maxidx] < a[i] :
            maxidx = i
    return maxidx

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(findmaxidx(v))

# problem

# 2-1

def findmin(a) :
    min = a[0]
    n = len(a)
    for i in range(1, n) :
        if a[i] < min :
            min = a[i]
    return min

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(findmin(v))