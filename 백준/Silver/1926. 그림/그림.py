from collections import deque

row, col = map(int, input().split())
draw = [list(map(int, input().split())) for _ in range(row)]

total = 0
largest = 0
visited = [[False]*col for _ in range(row)]

for r in range(row):
    for c in range(col):
        if draw[r][c] == 1 and not visited[r][c]: # 새 그림 시작점
            total+=1
            q = deque([(r, c)])
            visited[r][c] = True
            area = 1

            while q:
                x,y = q.popleft()
                for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                    nx, ny = x+dx, y+dy
                    if 0<=nx<row and 0<=ny<col:
                        if draw[nx][ny] == 1 and not visited[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny] = True
                            area += 1

            largest = max(area, largest)

print(total)
print(largest)