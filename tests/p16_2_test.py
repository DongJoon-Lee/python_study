from program.p16_2 import solve_maze

def test_solve_maze():

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

    assert solve_maze(maze,'a','p') == 'aeimnjfghlp'