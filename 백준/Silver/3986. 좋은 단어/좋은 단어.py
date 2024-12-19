import sys

n = int(sys.stdin.readline().rstrip())
good = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    stack = []
    for i in word:
        if not len(stack):
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        good += 1
print(good)