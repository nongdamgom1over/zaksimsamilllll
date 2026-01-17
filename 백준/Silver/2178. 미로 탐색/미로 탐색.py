from collections import deque

r, c = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(r)]

dist = [[0] * c for _ in range(r)]
q = deque([(0,0)])
dist[0][0] = 1

while q:
    x, y = q.popleft()

    for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
        nx, ny = x+dx, y+dy
        if 0<=nx<r and 0<=ny<c:
            if arr[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))


print(dist[r-1][c-1])