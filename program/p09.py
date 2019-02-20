def find_idx(a, b) :
    n = len(a)
    for i in range(n) :
        if b < a[i] :
            return i
    return n

def isort(a) :
    res = []
    while a :
        friend = a.pop(0)
        idx = find_idx(res, friend)
        res.insert(idx, friend)
    return res

d = [2,4,5,1,3]
print(isort(d)) # [1,2,3,4,5]


def isort2(a) :
    n = len(a)
    for i in range(1,n) :
        friend = a[i]
        j = i-1
        while 0 <= j and friend < a[j] :
            a[j+1] = a[j]
            j -= 1
        a[j+1] = friend

d = [2,4,5,1,3]
isort2(d)
print(d) # [1,2,3,4,5]

# Problem

# 9-2

def isort3(a) :
    n = len(a)
    for i in range(1,n) :
        friend = a[i]
        j = i-1
        while 0 <= j and a[j] < friend :
            a[j+1] = a[j]
            j -= 1
        a[j+1] = friend

d = [2,4,5,1,3]
isort3(d)
print(d) # 5,4,3,2,1