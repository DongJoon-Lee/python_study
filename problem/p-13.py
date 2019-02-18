# 큐와 스택을 사용하지 않고 회문인지 아닌지 알아보기

def palindrome(a):
    ans = []
    for x in a:
        if x.isalpha():
            ans.append(x.lower())
    n = len(ans)
    for x in range(n//2):
        if ans[x] != ans[n-1-x]:
            return False
    return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam"))
print(palindrome("Madam, I am Adam"))