# 7-1

# 프로그램 7-1에서 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 만들기
# 입력 : 리스트 a, 찾는 값 b
# 출력 : 찾으면 위치의 리스트, 못찾으면 -1

def search_list(a,b):
    return_list = []
    i = len(a)
    for x in range(i):
        if a[x] == b:
            return_list.append(x)
    return return_list


v = [17,92,18,33,58,7,33,42]
print(search_list(v,18))
print(search_list(v,33))
print(search_list(v,900))


# 7-2

# 7-1의 프로그램 복잡도는 최악의 경우를 계산했을때 O(n)이다. 


# 7-3

# 학생 번호와 이름이 리스트로 주어졌을 때 학생 번호를 입력하면 학생의 이름을 순차 탐색으로 찾아 돌려주는 함수
# 번호 없으면 ?
# 입력 : 학생 번호, 학생 번호 리스트, 학생 이름 리스트
# 출력 : 학생 이름

def find_name(a,b,c):
    i = len(b)
    for x in range (i):
        if a == b[x]:
            return c[x]
    return "?"


stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(find_name(14,stu_no,stu_name))
print(find_name(15,stu_no,stu_name))