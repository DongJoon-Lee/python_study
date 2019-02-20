# p16-1-maze.py

def smaze(a, start, end) :
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu :
        ans = qu.pop(0)
        v = ans[-1]
        if v == end :
            return ans
        for i in a[v] :
            if i not in done :
                qu.append(ans + i)
                done.add(i)
    return '?'


maze= {
    'a' : ['e'],
    'b' : ['c', 'f'],
    'c' : ['b','d'],
    'd' : ['c'],
    'e' : ['a', 'i'],
    'f' : ['b', 'g', 'j'],
    'g' : ['f', 'h'],
    'h' : ['g', 'l'],
    'i' : ['e', 'm'],
    'j' : ['f', 'k', 'n'],
    'k' : ['j', 'o'],
    'l' : ['h', 'p'],
    'm' : ['i', 'n'],
    'n' : ['m', 'j'],
    'o' : ['k'],
    'p' : ['l']
}

print(smaze(maze,'a','p'))