from collections import deque
def solution(maps):
    answer = 0
    row,col = len(maps), len(maps[0])
    dist = [[0]*col for _ in range(row)]
    q = deque([(0,0)])
    dist[0][0] = 1

    while q:
        x,y = q.popleft()
        if (x,y) == (row-1,col-1):
            return dist[x][y]
        for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nx, ny = x+dx, y+dy
            if 0<=nx<row and 0<=ny<col:
                if dist[nx][ny] == 0 and maps[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))

    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))