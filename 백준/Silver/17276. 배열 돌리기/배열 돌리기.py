import sys
from copy import deepcopy
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N, rotate = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 음수 회전을 양수로 변환
    if rotate < 0:
        rotate = 360 + rotate

    # 45의 배수만큼 반복
    r = rotate // 45

    # 제자리일 경우 그대로 출력
    if rotate == 0 or rotate == 360:
        for row in arr:
            print(*row)
        continue

    # 반복적으로 회전 처리
    for _ in range(r):
        result = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j:  # 주 대각선 -> 중앙 열
                    result[i][j] = arr[N // 2][j]
                elif i == N // 2:  # 중앙 행 -> 부 대각선
                    result[i][j] = arr[N - j - 1][j]
                elif i + j == N - 1:  # 부 대각선 -> 중앙 열
                    result[i][j] = arr[i][N // 2]
                elif j == N // 2:  # 중앙 열 -> 주 대각선
                    result[i][j] = arr[i][i]
                else:  # 나머지 유지
                    result[i][j] = arr[i][j]
        arr = deepcopy(result)

    # 결과 출력
    for row in arr:
        print(*row)
