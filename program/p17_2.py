# p17-1-fakecoin.py

def weigh(a,b,c,d) :
    fake = 29
    if a <= fake and fake <= b :
        return -1
    elif c <= fake and fake <= d :
        return 1
    return 0

def find_fake(left, right) :
    for i in range(left+1, right+1) :
        res = weigh(left, left, i, i)
        if res == -1 :
            return left
        elif res == 1 :
            return i
    return -1

n = 100
print(find_fake(1,100))

# p17-2-fakecoin.py

def weigh2(a,b,c,d) :
    fake = 29
    if a <= fake and fake <= b :
        return -1
    elif c <= fake and fake <= d :
        return 1
    return 0

def find_fake2(left, right) :
    if left == right : 
        return left
    
    mid = (left + right) // 2
    l1 = left
    r1 = mid-1
    l2 = mid+1
    r2 = right

    result = weigh2(l1,r1,l2,r2) 
    if result == -1 :
        return find_fake(l1,r1)
    elif result == 1 :
        return find_fake(l2, r2)
    else :
        return mid
    
n = 100
print(find_fake2(0,100))