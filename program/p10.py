def msort(a) :
    n = len(a)

    if n <= 1 :
        return a
    
    m = n//2
    a1 = msort(a[:m])
    a2 = msort(a[m:])
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
print(msort(d)) # 1,2,3,4,5,6,7,8,9,10

def msort2(a) :
   
    n = len(a)

    if n <= 1 :
        return

    m = n//2
    a1 = a[:m]
    a2 = a[m:]
    msort2(a1)
    msort2(a2)

    n1 = 0
    n2 = 0
    na = 0
    while n1 < len(a1) and n2 < len(a2) :
        if a1[n1] < a2[n2] :
            a[na] = a1[n1]
            na += 1
            n1 += 1
        else :
            a[na] = a2[n2]
            na += 1
            n2 += 1
    while n1 < len(a1) :
        a[na] = a1[n1]
        na += 1
        n1 += 1
    while n2 < len(a2) :
        a[na] = a2[n2]
        na += 1
        n2 += 1

d = [6,8,3,9,10,1,2,4,7,5]
msort2(d)
print(d) # 1,2,3,4,5,6,7,8,9,10

# Problem

# 10-1

def msort3(a) :
   
    n = len(a)

    if n <= 1 :
        return

    m = n//2
    a1 = a[:m]
    a2 = a[m:]
    msort3(a1)
    msort3(a2)

    n1 = 0
    n2 = 0
    na = 0
    while n1 < len(a1) and n2 < len(a2) :
        if a2[n2] < a1[n1] :
            a[na] = a1[n1]
            na += 1
            n1 += 1
        else :
            a[na] = a2[n2]
            na += 1
            n2 += 1
    while n1 < len(a1) :
        a[na] = a1[n1]
        na += 1
        n1 += 1
    while n2 < len(a2) :
        a[na] = a2[n2]
        na += 1
        n2 += 1

d = [6,8,3,9,10,1,2,4,7,5]
msort3(d)
print(d) # 10, 9,8,7,6,5,4,3,2,1