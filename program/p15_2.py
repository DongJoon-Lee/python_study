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

# p15-1-friend.py

def print_all_friend(a, start) :
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu :
        p = qu.pop(0)
        print(p)
        for x in a[p] :
            if x not in done :
                qu.append(x)
                done.add(x)



print_all_friend(fr_info, 'Summer')
print()
print_all_friend(fr_info, 'Jerry')

# p15-2-friend.py

def print_all_friend2(a, start) :
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu :
        (o,p) = qu.pop(0)
        print(o, p)
        for x in a[o] :
            if x not in done :
                done.add(x)
                qu.append((x, p+ 1))

print_all_friend2(fr_info, 'Summer')
print()
print_all_friend2(fr_info, 'Jerry')


# Problem

# 15-1

gr_info = {
    1 : [2,3],
    2 : [1,4,5],
    3 : [1],
    4 : [2],
    5 : [2]
}

def print_graph(a, start) :
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu :
        p = qu.pop(0)
        print(p)
        for x in a[p] :
            if x not in done :
                qu.append(x)
                done.add(x)

print_graph(gr_info, 1)