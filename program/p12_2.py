# p12-1-bsearch.py

def bsearch(a, x) :
    startidx = 0
    endidx = len(a)-1
    while startidx <= endidx :
        mididx = (startidx + endidx) // 2
        if x == a[mididx] :
            return mididx
        elif x < a[mididx] :
            endidx = mididx - 1
        else :
            startidx = mididx + 1
    return -1

d = [1,4,9,16,25,36,49,64,81]
print(bsearch(d, 36)) # 5
print(bsearch(d, 50)) # -1


# Problem

# 12-1

def bsearch_sub(a, x, start, end) :
    mid = (start + end) // 2
    if start <= end :
        if a[mid] == x :
            return mid
        elif a[mid] < x :
            return bsearch_sub(a, x, mid+1, end)
        else :
            return bsearch_sub(a, x, start, mid-1)
    return -1
    
def bsearch2(a, x) :
    return bsearch_sub(a, x, 0, len(a)-1)

d = [1,4,9,16,25,36,49,64,81]
print(bsearch2(d, 36)) # 5
print(bsearch2(d, 50)) # -1