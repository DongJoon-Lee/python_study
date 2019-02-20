# # p13-1-palindrome.py

def palindrome(a) :
    qu = []
    st = []
    for i in a :
        if i.isalpha() :
            qu.append(i.lower())
            st.append(i.lower())
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
    qu = []
    for i in a :
        if i.isalpha() :
            qu.append(i.lower())
    mid = len(qu)//2
    for i in range(mid) :
        if qu[i] != qu[-i-1] :
            return False
    return True

print(palindrome2("Wow"))
print(palindrome2("Madam, I'm Adam."))
print(palindrome2("Madam, I am Adam."))