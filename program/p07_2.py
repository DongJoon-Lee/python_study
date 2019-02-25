# # p07-1-search.py

def search_list(a, b) :
    n = len(a)
    for i in range(n) :
        if b == a[i] :
            return i
    return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18)) # 2
print(search_list(v, 33)) # 3
print(search_list(v, 900)) # -1

# Problem

# 7-1

def search_list2 (a, b) :
    n = len(a)
    res = []
    for i in range(n) :
        if b == a[i] :
            res.append(i)
    return res

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list2(v, 18)) # [2]
print(search_list2(v, 33)) # [3, 6]
print(search_list2(v, 900)) # []

# 7-3

def search_name(a, b, c) :
    n = len(a)
    for i in range(n) :
        if c == a[i] :
            return b[i]
    return '?'

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(search_name(stu_no, stu_name, 67)) # Mike
print(search_name(stu_no, stu_name, 106)) # ?