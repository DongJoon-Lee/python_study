from program.p16 import smaze

def test_smaze():
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

    assert smaze(maze,'a','p') == 'aeimnjfghlp'