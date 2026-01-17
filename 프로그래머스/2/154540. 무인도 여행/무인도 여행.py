from collections import deque

def solution(maps):
    answer = []
    row = len(maps)
    col = len(maps[0])
    visited = [[False] * col for _ in range(row)]
    for r in range(row):
        for c in range(col):
            if maps[r][c] != 'X' and not visited[r][c]:
                q = deque([(r,c)])
                visited[r][c] = True
                total = 0

                while q:
                    x, y = q.popleft()
                    total += int(maps[x][y])

                    for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<row and 0<=ny<col:
                            if not visited[nx][ny] and maps[nx][ny] != 'X':
                                visited[nx][ny] = True
                                q.append((nx,ny))
                answer.append(total)

    return sorted(answer) if answer else [-1]

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))