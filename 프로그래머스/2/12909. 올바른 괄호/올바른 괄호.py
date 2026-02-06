def solution(s):
    answer = True

    stack = []
    for ch in s:
        if ch == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False

    return True

s = "()()"
print(solution(s)) #true
s = "(())()"
print(solution(s)) #true
s = ")()("
print(solution(s)) #true
s = "(()("
print(solution(s)) #true