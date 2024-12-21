from collections import deque

# 입력 받기
N = int(input())

# 큐 초기화
queue = deque(range(1, N + 1))

# 큐 처리
while len(queue) > 1:
    queue.popleft()  # 제일 위의 카드를 버림
    queue.append(queue.popleft())  # 그 다음 카드를 제일 아래로 이동

# 마지막 남은 카드 출력
print(queue[0])
