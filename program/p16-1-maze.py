# 미로 찾기
# 문자열로 저장.....흠

def smaze(g, start, end):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        v = p[-1] # 이어지면 문자열됨, 가장 끝에서 가는 경로 선택하므로
        if v == end:
            return p
        for i in g[v] :
            if i not in done :
                qu.append(p + i)
                done.add(i)
    return "?"

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