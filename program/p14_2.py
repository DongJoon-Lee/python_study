# p14-1-samename.py

def samename(a) :
    name = dict()
    for x in a :
        if x not in name :
            name[x] = 1
        else :
            name[x] += 1
    res = set()
    for x in name :
        if 2 <= name[x] :
            res.add(x)
    return res

name = ["Tom", "Jerry", "Mike", "Tom"]
print(samename(name)) # {'Tom'}

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(samename(name2)) # {'Mike', 'Tom'}


# Problem

# 14-1

def find_stu(num, name, a) :
    res = dict()
    for i in range(len(num)) :
        res[num[i]] = name[i]
    for x in res :
        if a in res :
            return res[a]
    return '?'

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(find_stu(stu_no, stu_name, 67)) # Mike
print(find_stu(stu_no, stu_name, 101)) # ?
