# p01-1-sum.py



def sum1(n) :
    sum = 0
    for i in range (1, n+1) :
        sum += i
    return sum

print(sum1(10))
print(sum1(100))

# p01-2-sum.py



def sum2(n) :
    sum = n*(n+1)/2
    return sum

print(sum2(10))
print(sum2(100))




# Problem

# 1-1


def pro1(n) : 
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    return sum

print(pro1(10))
