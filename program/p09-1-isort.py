# 쉽게 설명한 삽입 정렬
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

def find_ind(a,b): # 리스트 a, 리스트 내의 숫자 b
    for i in range (len(a)):
        if b < a[i]:
            return i
    return len(a) # b가 모든 리스트 a 내의 값보다 크면 가장 뒤에 넣어야 한다. (len(a)-1이 아닌 이유는 len(a)-1에다 넣으면 a의 마지막 값이 하나 밀리기 때문에)

def isort(a):
    result = []
    while a :
        b = a.pop(0)
        new_ind = find_ind(result,b)
        result.insert(new_ind,b)
    return result

v = [2,4,5,1,3]
print(isort(v))
