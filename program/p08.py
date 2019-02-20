def find_min_idx(a) :
    min_idx = 0
    n = len(a)
    for i in range(n) :
        if a[i] < a[min_idx] :
            min_idx = i
    return min_idx

def ssort(a) :
    res = []
    while a :
        min_idx = find_min_idx(a)
        min = a.pop(min_idx)
        res.append(min)
    return res

d = [2,4,5,1,3]
print(ssort(d)) #[1,2,3,4,5]


def ssort2(a) :
    n = len(a)
    for i in range(n-1) :
        min_idx = i
        for j in range(i+1, n) :
            if a[j] < a[min_idx] :
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

d = [2,4,5,1,3]
ssort2(d)
print(d) # [1,2,3,4,5]

# Problem

# 8-2

def ssort3(a) :
    n = len(a)
    for i in range(n-1) :
        max_idx = i
        for j in range(i+1, n) :
            if a[max_idx] < a[j] :
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

d = [2,4,5,1,3]
ssort3(d)
print(d)# [5,4,3,2,1]
