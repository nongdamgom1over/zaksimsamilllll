queue = []
rear = 0
fr = 0

def push(X):
    global rear
    queue.append(X)  # 정수 X를 큐에 넣는 연산
    rear = len(queue)
    return X

def pop():
    global fr
    if rear == fr:  # 큐가 비어 있는 경우
        return -1
    res = fr
    fr += 1
    return queue[res]

def size():
    return rear - fr

def empty():
    if rear == fr:
        return 1
    else:
        return 0

def front():
    if rear == fr:  # 큐가 비어 있는 경우
        return -1
    else:
        return queue[fr]

def back():
    if rear == fr:  # 큐가 비어 있는 경우
        return -1
    else:
        return queue[rear - 1]  # `rear`는 배열의 길이를 나타내므로 마지막 원소는 `rear - 1` 위치

# 명령어 처리 부분
import sys
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        push(int(command[1]))
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'front':
        print(front())
    elif command[0] == 'back':
        print(back())
