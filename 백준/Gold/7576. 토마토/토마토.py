from collections import deque
import sys

col, row = map(int, input().split())
tomates = [list(map(int, input().split())) for _ in range(row)]
days = [[0]*col for _ in range(row)]

q = deque()
for r in range(row):
    for c in range(col):
        if tomates[r][c] == 1:
            q.append((r,c))

while q:
    x,y = q.popleft()
    for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
        nx, ny = x+dx, y+dy
        if 0<=nx<row and 0<=ny<col:
            if tomates[nx][ny] == 0: # 안익음
                tomates[nx][ny] = 1 # 익음
                q.append((nx,ny))
                days[nx][ny] = days[x][y] + 1

for r in range(row):
    for c in range(col):
        if tomates[r][c] == 0: #안익은아이있다면
            print(-1)
            sys.exit(0)

print(max(map(max, days)))