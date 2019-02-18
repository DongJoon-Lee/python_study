# 문제 7-3을 딕셔너리를 사용하여 풀기

# stu_no = [39, 14, 67, 105]
# stu_name = ["Justin", "John", "Mike", "Summer"]

def find_name(x) :
    name = dict()
    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]
    for i in range(4):
        name[stu_no[i]] = stu_name[i]
    if x in name:
        return name[x]
    return "?"


print(find_name(39))
print(find_name(14))
print(find_name(50))