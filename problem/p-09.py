# 9-1

# 일반적인 삽입 정렬 알고리즘을 사용해서 리스트 [2,4,5,1,3]을 정렬하는 과정을 적기

# 1번 인덱스를 잡고, 앞에 값과 비교한다. 
# 앞의 값과 비교했을때, 앞의 값이 더 작으면 둘의 순서를 바꾼다. 
# 다시 그 앞의 것과 비교하여, 더 이상 작지 않은 수가 나올 때까지 바꾼다.  신기하다.

# 9-2

# 내림차순 정렬로 바꾸려면 어느 부분을 바꿔야?
# 내림차순은 큰 값이 앞으로 넘어가면 된다. 

def isort(a) :
    i = len(a)
    for x in range(1,i):
        key = a[x]
        j = x-1
        while j >= 0 and a[j] < key : # key가 고정이다.
            a[j +1] = a[j]
            j -= 1
            a[j+1] = key # 하나씩 옆으로 밀어줌,, 어렵다 똑똑하구만
            

v = [2,4,5,1,3]
isort(v)
print(v)