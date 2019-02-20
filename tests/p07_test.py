from program.p07 import search_list, search_list_all, find_stu

def test_search_list():
    v = [17, 92, 18, 33, 58, 7, 33, 42]
    assert search_list(v, 18) == 2
    assert search_list(v, 33) == 3
    assert search_list(v, 900) == -1

def test_search_list_all():
    v = [17, 92, 18, 33, 58, 7, 33, 42]
    assert search_list_all(v, 18) == [2]
    assert search_list_all(v, 33) == [3, 6]
    assert search_list_all(v, 900) == []

def test_find_stu():
    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]
    assert find_stu(stu_no, stu_name, 67) == 'Mike'
    assert find_stu(stu_no, stu_name, 101) == '?'