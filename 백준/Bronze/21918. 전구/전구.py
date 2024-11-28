import sys

# 입력 받기
N, M = map(int, input().split())
state = list(map(int, input().split()))  # 전구 상태를 정수 리스트로 변환

# 명령어 함수 정의
def command1(i, x):
    state[i - 1] = x

def command2(l, r):
    for i in range(l - 1, r):
        state[i] = 1 - state[i]  # 0과 1을 토글

def command3(l, r):
    for i in range(l - 1, r):
        state[i] = 0

def command4(l, r):
    for i in range(l - 1, r):
        state[i] = 1

# 명령어 처리
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        command1(b, c)
    elif a == 2:
        command2(b, c)
    elif a == 3:
        command3(b, c)
    elif a == 4:
        command4(b, c)

# 결과 출력
print(*state)
