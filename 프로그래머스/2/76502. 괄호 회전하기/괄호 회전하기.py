def solution(s):
    answer = 0
    n = len(s)
    s=s*2
    for i in range(n):
        st = s[i:i + n]
        stack = []
        valid = True

        for j in range(n):
            c = st[j]
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    valid = False
                    break
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    valid = False
                    break

        if valid and not stack:
            answer += 1
    return answer

s= "[](){}"
print(solution(s))