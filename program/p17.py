# p17-1-fakecoin.py

def weigh(a,b,c,d) :
    fake = 29 ##
    if a <= fake and fake <= b :
        return -1
    elif c <= fake and fake <= d :
        return 1
    return 0

def find_fake(l, r) :
    for i in range(l+1, r+1) :
        result = weigh(l, l, i, i)
        if result == -1 :
            return l
        elif result == 1 :
            return i
    return -1

n = 100
print(find_fake(0, n))

# p17-2-fakecoin.py

def weigh(a,b,c,d) :
    fake = 29 ##
    if a <= fake and fake <= b :
        return -1
    elif c <= fake and fake <= d :
        return 1
    return 0

def find_fake2(l, r) :
    if l == r :
        return l
    
    m = (l + r) // 2
    left1 = l
    right1 = m-1
    left2 = m
    right2 = r-1
    
    result = weigh(left1, right1, left2, right2)
    if result == -1 :
        return find_fake2(left1, right1)
    elif result == 1 :
        return find_fake2(left2, right2)
    return r

n = 100
print(find_fake2(0, 100))