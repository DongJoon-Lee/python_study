from program.p03 import samename

def test_samename():
    name = ["Tom", "Jerry", "Mike", "Tom"]
    assert samename(name) == {'Tom'}
    name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
    assert samename(name) == {'Tom', 'Mike'}