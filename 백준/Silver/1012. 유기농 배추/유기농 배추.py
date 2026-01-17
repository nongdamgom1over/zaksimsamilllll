from collections import deque
import sys
input = sys.stdin.readline

T=int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]

    for _ in range(K):
        x,y =map(int, input().split())
        field[y][x] = 1

    worms = 0
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1:
                worms+=1
                q = deque([(r,c)])
                field[r][c] = 0 # visited 대신 0으로 변경

                while q:
                    x,y = q.popleft()
                    for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<N and 0<=ny<M and field[nx][ny]==1:
                            field[nx][ny] = 0
                            q.append((nx,ny))

    print(worms)