# p10-1-msort.py

def msort(a) :
    n = len(a)
    if n <= 1 :
        return a
    mid = n // 2
    
    a1 = msort(a[:mid])
    a2 = msort(a[mid:])

    res = []
    while a1 and a2 :
        if a1[0] < a2[0] :
            res.append(a1.pop(0))
        else :
            res.append(a2.pop(0))
    while a1 : 
        res.append(a1.pop(0))
    while a2 :
        res.append(a2.pop(0))
    return res

d = [6,8,3,9,10,1,2,4,7,5]
print(msort(d)) # [1,2,3,4,5,6,7,8,9,10]

# p10-2-msort.py

def msort_c(a) :
    n = len(a)
    if n <= 1 :
        return 
    mid = n // 2
    a1 = a[:mid]
    a2 = a[mid:]
    msort_c(a1)
    msort_c(a2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(a1) and i2 < len(a2) :
        if a1[i1] < a2[i2] :
            a[ia] = a1[i1]
            ia +=1
            i1 +=1
        else :
            a[ia] = a2[i2]
            ia +=1
            i2 +=1
    while i1 < len(a1) :
        a[ia] = a1[i1]
        ia += 1
        i1 += 1
    while i2 < len(a2) :
        a[ia] = a2[i2]
        ia += 1
        i2 += 1

d = [6,8,3,9,10,1,2,4,7,5]
msort_c(d)
print(d) # [1,2,3,4,5,6,7,8,9,10]


# Problem

# 10-1

def msort2(a) :
    n = len(a)
    if n <= 1 :
        return a
    mid = n // 2
    
    a1 = msort2(a[:mid])
    a2 = msort2(a[mid:])

    res = []
    while a1 and a2 :
        if a2[0] < a1[0] :
            res.append(a1.pop(0))
        else :
            res.append(a2.pop(0))
    while a1 : 
        res.append(a1.pop(0))
    while a2 :
        res.append(a2.pop(0))
    return res

d = [6,8,3,9,10,1,2,4,7,5]
print(msort2(d)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def msort_c2(a) :
    n = len(a)
    if n <= 1 :
        return 
    mid = n // 2
    a1 = a[:mid]
    a2 = a[mid:]
    msort_c2(a1)
    msort_c2(a2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(a1) and i2 < len(a2) :
        if  a2[i2] < a1[i1] :
            a[ia] = a1[i1]
            ia +=1
            i1 +=1
        else :
            a[ia] = a2[i2]
            ia +=1
            i2 +=1
    while i1 < len(a1) :
        a[ia] = a1[i1]
        ia += 1
        i1 += 1
    while i2 < len(a2) :
        a[ia] = a2[i2]
        ia += 1
        i2 += 1

d = [6,8,3,9,10,1,2,4,7,5]
msort_c2(d)
print(d) # [1,2,3,4,5,6,7,8,9,10]