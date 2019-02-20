# p12-1-bsearch.py

def bsearch(a, x) :
    n = len(a)
    start = 0
    end = n-1
    while start <= end :
        mid = (start + end) // 2
        if a[mid] == x :
            return mid
        elif a[mid] < x :
            start = mid + 1
        else :
            end = mid -1
    return -1

d= [1,4,9,16,25,36,49,64,81]
print(bsearch(d, 36)) # 5
print(bsearch(d, 50)) # -1


# problem

# 12-1

def bsearch_sub(a, x, start, end) :
    if end < start :
        return -1

    mid = (start + end)//2

    if a[mid] == x :
        return mid
    elif a[mid] < x :
        return bsearch_sub(a, x, mid+1, end)
    else :
        return bsearch_sub(a, x, start, mid-1)
    
def bsearch2(a, x) :
    return bsearch_sub(a, x, 0, len(a)-1)
    
d= [1,4,9,16,25,36,49,64,81] # len(a) = 9
print(bsearch2(d, 36)) # 5
print(bsearch2(d, 50)) # -1