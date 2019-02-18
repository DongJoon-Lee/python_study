# 15-1
# 그래프를 탐색하는 프로그램 만들기, 시작 꼭짓점 1

gr_info = {
    1 : [2,3],
    2 : [1,4,5],
    3 : [1],
    4 : [2],
    5 : [2]
}

def graph(a, b):
    qu = []
    done = set()

    qu.append(b)
    done.add(b)

    while qu:
        c = qu.pop(0)
        print(c)
        for x in a[c]:
            if x not in done:
                qu.append(x)
                done.add(x)

graph(gr_info, 1)

# 15-2

#초기값이 1이므로, qu 리스트와 done 집합에 1을 포함시킨다. 
# qu가 비어있지 않으므로 while 안으로 넘어가고, c가 qu[0]이므로 1이다. 
# 1의 아래에는 2와 3이 있고, 둘 다 done에 없으므로 done에 추가하고 qu에도 추가한다. 
# 이를 반복하면, 2 아래에는 4와 5가 있고 3 아래에는 아무것도 없다. 
# 1 - 2 - 3 - 4 - 5의 순서대로 출력된다. 