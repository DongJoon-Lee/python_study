# 큐와 스택의 차이
# 큐(Queue) - 줄 서기
# 먼서 선 사람이 먼저 나감. (First In First Out)

# 스택(Stack) - 접시 쌓기
# 나중에 쌓인 접시가 먼저 나감. (Last In First Out)

# 리스트로 큐와 스택 사용

# 큐
# 초기화 
# qu = []
# 자료 넣기
# qu.append(x)
# 자료 빼기
# x = qu.pop(0)

# 스택
# 초기화
# st = []
# 자료 넣기
# st.append(x)
# 자료 빼기
# x = st.pop()

def palindrome(a):
    qu = []
    st = []
    for x in a:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    while qu :
        if qu.pop(0) != st.pop():
            return False
    return True
# x.lower() -> x를 소문자로 바꾼다. 
# x.isalpha() -> 공백, 숫자, 특수문자를 걸러낸다. 
# 오...

print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam"))
print(palindrome("Madam, I am Adam"))