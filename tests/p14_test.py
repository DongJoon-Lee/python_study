from program.p14 import samename, find_stu

def test_samename():
    name = ['Tom', 'Jerry', 'Mike', 'Tom']
    assert samename(name) == {'Tom'}
    name2 = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike']
    assert samename(name2) == {'Tom', 'Mike'}

def test_find_stu():
    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]
    assert find_stu(stu_no, stu_name, 67) == 'Mike'
    assert find_stu(stu_no, stu_name, 101) == '?'