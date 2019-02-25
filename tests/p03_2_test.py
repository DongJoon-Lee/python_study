from program.p03_2 import samename

name = ["Tom", "Jerry", "Mike", "Tom"]
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]

def test_samename():
    assert samename(name) == {'Tom'}
    assert samename(name2) == {'Tom', 'Mike'}