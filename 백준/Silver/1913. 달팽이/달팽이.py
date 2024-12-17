import sys

# 입력 받기
n = int(sys.stdin.readline().rstrip())  # 달팽이 배열 크기
point = int(sys.stdin.readline().rstrip())  # 찾고자 하는 숫자

# 달팽이 배열 초기화
snail = [[0]*n for _ in range(n)]

# 방향 설정 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시작 위치 (중앙)
x, y = n // 2, n // 2
snail[x][y] = 1  # 중앙에 숫자 1 채우기
num = 2  # 다음에 채울 숫자

# 반복 초기화
re = 1  # 각 방향으로 이동하는 반복 횟수
i = 0  # dx, dy의 방향 인덱스 (0: 상, 1: 우, 2: 하, 3: 좌)
answer = [x+1, y+1]  # 찾고자 하는 숫자의 좌표 (1-based)
flag = 0  # 반복문 종료를 위한 플래그

# 달팽이 채우기
while flag == 0:  # 종료 플래그가 설정되지 않으면 반복
    for _ in range(2):  # 같은 이동 거리로 2번 반복
        for _ in range(re):  # 현재 방향으로 re번 이동
            x += dx[i]  # 행 이동
            y += dy[i]  # 열 이동
            snail[x][y] = num  # 현재 위치에 숫자 채우기
            if num == point:  # 찾는 숫자 발견 시
                answer = [x+1, y+1]  # 좌표 저장 (1-based)
            if x == 0 and y == 0:  # 좌측 상단에 도달했을 때
                flag = 1  # 종료 플래그 설정
                break
            num += 1  # 다음 숫자로 증가
        if flag == 1:  # 플래그가 설정되면 반복 종료
            break
        i = (i + 1) % 4  # 방향 전환
    re += 1  # 반복 횟수 증가

# 결과 출력
for row in snail:  # 달팽이 배열 출력
    print(*row)
print(*answer)  # 찾는 숫자의 좌표 출력
