# 친구 리스트에서 자신의 모든 친구 찾기
# 입력 : 친구 관계 그래프 g, 모든 친구를 찾을 자신
# 출력 : 모든 친구의 이름
# 흠....

def friend(g, x):
    qu = []
    done = set()

    qu.append(x)
    done.add(x)
    
    while qu:
        n = qu.pop(0)
        print(n)
        for i in g[n] :
            if i not in done :
                qu.append(i)
                done.add(i)


# 친구 관계 리스트

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