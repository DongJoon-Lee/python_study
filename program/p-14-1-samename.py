# 딕셔너리
# 키 - 값 구조
# d = {"Justin" : 13, "John" : 10, "Mike" : 9}

# 빈 딕셔너리
# d = {}
# d = dict()

# 딕셔너리에 새 값 추가
# d["Summer"] = 1
# 중복되면 기존 값 사라짐

# 값 제거
# del d[key]

# 자료 초기화
# d.clear()

# 자료 있는지 확인
# key in d


# 두 번 이상 나온 이름 찾기
# 입력 : 이름이 n개 들어있는 리스트
# 출력 : 반복되는 이름의 집합

def samename(a) :
    name = dict()
    for n in a:
        if n in name:
            name[n] += 1
        else :
            name[n] = 1
    res = set() # 집합 만들기
    for n in name:
        if name[n] >= 2:
            res.add(n)
    
    return res

name = ["Tom", "Jerry", "Mike", "Tom"]
print(samename(name))

name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(samename(name))