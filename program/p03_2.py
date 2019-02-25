# p03-1-samename.py

def samename(a) :
    same = set()
    n = len(a)
    for i in range(n-1) :
        for j in range(i+1, n) :
            if a[i] == a[j] :
                same.add(a[i])
    return same

name = ["Tom", "Jerry", "Mike", "Tom"]
print(samename(name)) # {'Tom'}

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(samename(name2)) # {'Tom', 'Mike'}

# Problem

# 3-1

def printfriend(a) :
    n = len(a)
    for i in range(n-1) :
        for j in range(i+1, n) :
            print(a[i], '-', a[j])

printfriend(["Tom", "Jerry", "Mike"])