import sys

input = sys.stdin.readline

# 배열 크기 입력
n, m = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 누적 합 배열 생성
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

# 쿼리 처리
k = int(input().rstrip())
for _ in range(k):
    i, j, x, y = map(int, input().rstrip().split())
    result = dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1]
    print(result)
