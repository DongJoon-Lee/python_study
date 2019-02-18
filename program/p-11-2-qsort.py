# 퀵 정렬...
# 이상한 방식
# 예시 코드 봤음...

def q_sort(a, start, end):
    if end<= start:
        return

    pivot = a[end]
    i = start
    for j in range(start,end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    
    q_sort(a, start, i-1)
    q_sort(a, i+1, end)

def qsort(a):
    q_sort(a,0,len(a)-1)

d = [6,8,3,9,10,1,2,4,7,5]
qsort(d)
print(d)



# 편의상 기준을 마지막 친구로 잡았고, i는 0번 인덱스이다. 
# 만약 pivot보다 a[j]가 더 작다면, 기준인 친구가 그 친구보다 크므로 i는 한 칸 옆으로 이동한다. 
# 그렇지 않으면, i는 고정이고 j만 증가하게 된다. -> i와 j의 값이 차이가 난다. 
# 그 이후에 a[j]가 더 작은 값이 나오면, a[j]는 기준보다 작고, a[i]는 기준보다 크므로 둘을 바꿔준다!!!
# 그리고 기존 i값의 a[i]는 기준보다 작아지게 되므로 i를 +=1한다. 

# 마지막으로, a[end](기준값)과 i값을 바꿔주면 일차적인 정렬이 끝난다. 
# 그 이후에는 기준점을 중심으로 앞뒤로 나눠 반복한다. 

#그냥 리스트 새로 만들어서 하는게 더 편해보인다.... 어렵