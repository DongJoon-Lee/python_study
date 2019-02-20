# p14-1-samename.py

def samename(a) :
    dic = dict()
    res = set()
    for i in a :
        if i in dic :
            dic[i] += 1
        else :
            dic[i] = 1
    for i in dic :
        if 2 <= dic[i] :
            res.add(i)
    return res

name = ['Tom', 'Jerry', 'Mike', 'Tom']
print(samename(name)) # {'Tom'}
name2 = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike']
print(samename(name2)) # {'Tom', 'Mike'}


# Problem

# 14-1

def find_stu(a, b, c) :
    stu = dict()
    n = len(a)
    for i in range(n) :
        stu[a[i]] = b[i]
    if c in stu :
        return stu[c]
    return '?'

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(find_stu(stu_no, stu_name, 67)) # Mike
print(find_stu(stu_no, stu_name, 101)) # ?