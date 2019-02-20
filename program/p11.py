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
print(qsort(d))



# :(
# p11-2-qsort2.py

def qsort_sub(a, start, end) :
    if end <= start :
        return 
 
    pivot = a[end]
    p_loc = start
    for i in range(start, end) :
        if a[i] <= pivot : 
            a[i], a[p_loc] = a[p_loc], a[i]
            p_loc += 1
    a[p_loc], a[end] = a[end], a[p_loc]
    qsort_sub(a, start, p_loc-1)
    qsort_sub(a,p_loc+1, end)

def qsort2(a) :
    qsort_sub(a,0,len(a)-1)

d = [6,8,3,9,10,1,2,4,7,5]
qsort2(d)
print(d)


# Problem
# 11-1
# Bubble sort

def bsort(a):
    n = len(a)

    for i in range(n-1) :
        for j in range(n-1-i) :
            if a[j + 1] < a[j] :
                a[j], a[j+1] = a[j+1], a[j]
    

d = [6,8,3,9,10,1,2,4,7,5]
bsort(d)
print(d)