from program.p07_2 import search_list, search_list2, search_name

def test_search_list():
    v = [17, 92, 18, 33, 58, 7, 33, 42]

    assert search_list(v, 18) == 2
    assert search_list(v, 33) == 3
    assert search_list(v, 900) == -1

def test_search_list2():
    v = [17, 92, 18, 33, 58, 7, 33, 42]

    assert search_list2(v, 18) == [2]
    assert search_list2(v, 33) == [3,6]
    assert search_list2(v, 900) == []

def test_search_name():
    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]

    assert search_name(stu_no, stu_name, 67) == 'Mike'
    assert search_name(stu_no, stu_name, 106) == '?'