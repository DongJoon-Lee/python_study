# p03-1-samename.py

def samename(a) :
    n = len(a)
    res = set()
    for i in range (n-1) :
        for j in range(i+1, n) :
            if a[i] == a[j] :
                res.add(a[i])
    return res

name = ["Tom", "Jerry", "Mike", "Tom"]
print(samename(name)) # {'Tom'}
name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(samename(name)) # {'Tom', 'Mike'}

# Problem

# 3-1

def pro31(a) :
    n = len(a)
    for i in range(n-1) :
        for j in range(i+1, n) :
            print(a[i], '-', a[j])

v = ["Tom", "Jerry", "Mike"]
pro31(v)
# Tom - Jerry
# Tom - Mike
# Jerry - Mike

# 3-2
