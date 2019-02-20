from program.p13 import palindrome, palindrome2

def test_palindrome():
    assert palindrome("Wow") == True
    assert palindrome("Madam, I'm Adam.") == True
    assert palindrome("Madam, I am Adam.") == False

def test_palindrome2():
    assert palindrome2("Wow") == True
    assert palindrome2("Madam, I'm Adam.") == True
    assert palindrome2("Madam, I am Adam.") == False