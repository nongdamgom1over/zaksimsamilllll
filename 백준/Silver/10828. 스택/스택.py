import sys
N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push': # push 명령어인 경우 command[1]도 있음
        stack.append(command[1]) # 가장 위에 정수를 추가
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])