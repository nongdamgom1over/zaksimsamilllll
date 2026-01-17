from collections import deque
import sys

col, row = map(int, input().split())
tomates = [list(map(int, input().split())) for _ in range(row)]

q = deque()
for r in range(row):
    for c in range(col):
        if tomates[r][c] == 1: # 익은 애들 큐에 넣기
            q.append((r,c))

while q:
    x,y = q.popleft()
    for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
        nx, ny = x+dx, y+dy
        if 0<=nx<row and 0<=ny<col:
            if tomates[nx][ny] == 0: # 아직 안익은 토마토면
                q.append((nx,ny))
                tomates[nx][ny] = tomates[x][y] + 1

answer = 0
for r in range(row):
    for c in range(col):
        if tomates[r][c] == 0: # 안익은거 남아있으면
            print(-1)
            sys.exit(0)
        answer = max(answer, tomates[r][c])

print(answer-1)