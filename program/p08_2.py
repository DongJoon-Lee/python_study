# p08-1-ssort.py

def findminidx(a) :
    n = len(a)
    minidx = 0
    for i in range(1, n) :
        if a[i] < a[minidx] :
            minidx = i
    return minidx

def ssort(a) :
    res = []
    while a :
        minidx = findminidx(a)
        min = a.pop(minidx)
        res.append(min)
    return res

d = [2,4,5,1,3]
print(ssort(d)) # [1,2,3,4,5]


# p08-2-ssort.py

def ssort2_c(a) :
    n = len(a)
    for i in range(n-1) :
        minidx = i
        for j in range(i+1, n) :
            if a[j] < a[minidx] :
                minidx = j
        a[minidx], a[i] = a[i], a[minidx]

d = [2,4,5,1,3]
ssort2_c(d)
print(d)


# Problem

# 8-2

def findmaxidx2(a) :
    n = len(a)
    maxidx = 0
    for i in range(1, n) :
        if a[maxidx] < a[i] :
            maxidx = i
    return maxidx

def ssort2(a) :
    res = []
    while a :
        maxidx = findmaxidx2(a)
        max = a.pop(maxidx)
        res.append(max)
    return res

d = [2,4,5,1,3]
print(ssort2(d)) # [5,4,3,2,1]

def ssort2_c(a) :
    n = len(a)
    for i in range(n-1) :
        maxidx = i
        for j in range(i+1, n) :
            if a[maxidx] < a[j] :
                maxidx = j
        a[maxidx], a[i] = a[i], a[maxidx]

d = [2,4,5,1,3]
ssort2_c(d)
print(d)