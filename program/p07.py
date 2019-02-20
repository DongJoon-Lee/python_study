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

def search_list_all(a, b) :
    n = len(a)
    res = []
    for i in range(n) :
        if b == a[i] :
            res.append(i)
    return res

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list_all(v, 18)) # [2]
print(search_list_all(v, 33)) # [3, 6]
print(search_list_all(v, 900)) # []

# 7-3

def find_stu(a, b, c) :
    n = len(a)
    for i in range(n) :
        if c == a[i] :
            return b[i]
    return '?'

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(find_stu(stu_no, stu_name, 67)) # Mike
print(find_stu(stu_no, stu_name, 101)) # ?