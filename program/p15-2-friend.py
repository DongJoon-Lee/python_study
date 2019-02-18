# 15-1 + 친밀도 출력

def friend(g, x):
    qu = []
    done = set()

    qu.append((x, 0))
    done.add(x)

    while qu:
        (a, b) = qu.pop(0)
        print(a,b)
        for i in g[a]:
            if i not in done:
                qu.append((i, b + 1))
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

# 음.......