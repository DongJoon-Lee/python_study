# p13-1-palindrome.py

def palindrome(a) : 
    qu = []
    st = []
    for x in a :
        if x.isalpha() :
            qu.append(x.lower())
            st.append(x.lower())
    while qu :
        if qu.pop(0) != st.pop() :
            return False
    return True

print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))


# Problem

# 13-1

def palindrome2(a) :
    res = []
    for x in a :
        if x.isalpha() :
            res.append(x.lower())
    for i in range(len(res) // 2) :
        if res[i] != res[len(res)-1-i] :
            return False
    return True

print(palindrome2("Wow"))
print(palindrome2("Madam, I'm Adam."))
print(palindrome2("Madam, I am Adam."))