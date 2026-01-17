from collections import deque
def solution(maps):
    m, n = len(maps), len(maps[0])
    dist = [[0]*n for _ in range(m)]
    q = deque([(0,0)]) # 시작점
    dist[0][0] = 1

    while q:
        x, y = q.popleft()
        if (x,y) == (m-1,n-1): # 상대 진영 도착
            return dist[x][y]
        for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n:
                if dist[nx][ny] == 0 and maps[nx][ny] == 1:
                    q.append((nx,ny))
                    dist[nx][ny] = dist[x][y] + 1

    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))