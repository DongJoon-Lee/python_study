#1부터 n까지의 합을 구함

def sumN(a) :
    sum = 0
    for i in range(1, a+1):
        sum = sum+i
    return sum

print(sumN(10))
print(sumN(100))