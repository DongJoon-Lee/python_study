# p15-1-friend.py

def friend(a, start) :
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu :
        name = qu.pop(0)
        print(name)
        for i in a[name] :
            if i not in done :
                qu.append(i)
                done.add(i)

fr_info = {
    'Summer' : ['John', 'Justin', 'Mike'],
    'John' : ['Summer', 'Justin'],
    'Justin' : ['John', 'Summer', 'Mike', 'May'],
    'Mike' : ['Summer', 'Justin'],
    'May' : ['Justin', 'Kim'],
    'Kim' : ['May'],
    'Tom' : ['Jerry'],
    'Jerry' : ['Tom']
}

friend(fr_info, 'Summer')
print()
friend(fr_info, 'Jerry')

# p15-2-friend.py

def friend2(a, start) :
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu :
        (b, c) = qu.pop(0)
        print(b, c)
        for i in a[b] :
            if i not in done :
                qu.append((i, c+1))
                done.add(i)

friend2(fr_info, 'Summer')
print()
friend2(fr_info, 'Jerry')

# Problem

# 15-1

def graph(a, start) :
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu :
        b = qu.pop(0)
        print(b)
        for i in a[b] :
            if i not in done :
                qu.append(i)
                done.add(i)

gr_info = {
    1 : [2,3],
    2 : [1,4,5],
    3 : [1],
    4 : [2],
    5 : [2]
}

graph(gr_info, 1) # 1 2 3 4 5