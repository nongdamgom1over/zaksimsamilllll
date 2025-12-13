def solution(storage, requests):
    from collections import deque

    def remove_by_forklift(grid, target):
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        q = deque()

        # 1️⃣ 외부와 바로 맞닿은 빈 공간 탐색 시작
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == '.':
                    q.append((i, j))
                    visited[i][j] = True

        # 2️⃣ BFS로 외부 공간 확장
        while q:
            x, y = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if grid[nx][ny] == '.':
                        visited[nx][ny] = True
                        q.append((nx, ny))

        # 3️⃣ 외부 공간과 맞닿은 target 제거
        for i in range(n):
            for j in range(m):
                if grid[i][j] == target:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj]:
                            grid[i][j] = '.'
                            break

    def remove_by_crane(grid, target):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == target:
                    grid[i][j] = '.'

    grid = [list(row) for row in storage]

    for req in requests:
        target = req[0]
        if len(req) == 1:      # 지게차
            remove_by_forklift(grid, target)
        else:                  # 크레인
            remove_by_crane(grid, target)

    # 남은 컨테이너 개수
    return sum(cell != '.' for row in grid for cell in row)


storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
requests = ["A", "BB", "A"]
print(solution(storage, requests))