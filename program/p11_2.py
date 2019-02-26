# p11-1-qsort.py

def qsort(a) :
    n = len(a)
    if n <= 1 :
        return a
    pivot = a[-1]
    a1 = []
    a2 = []
    for i in range(n-1) :
        if a[i] < pivot :
            a1.append(a[i])
        else :
            a2.append(a[i])
    return qsort(a1) + [pivot] + qsort(a2)

d = [6,8,3,9,10,1,2,4,7,5]
print(qsort(d)) # [1,2,3,4,5,6,7,8,9,10]


# Problem

# 11-1

def bsort(a) :
    n = len(a)
    for i in range(n) :
        for j in range(n-1) :
            if a[j+1] < a[j] :
                a[j+1], a[j] = a[j], a[j+1]
    return a
d = [6,8,3,9,10,1,2,4,7,5]
print(bsort(d)) # [1,2,3,4,5,6,7,8,9,10]