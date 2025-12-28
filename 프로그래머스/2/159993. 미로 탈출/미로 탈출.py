from collections import deque
def solution(maps):
    row = len(maps) # 세로줄 수
    col = len(maps[0]) # 가로줄 수

    for r in range(row):
        for c in range(col):
            if maps[r][c] == 'S': # 시작점이면
                start = (r,c)
            elif maps[r][c] == 'L': # 레버칸
                lever = (r,c)
            elif maps[r][c] == 'E': # 출구칸
                exit = (r,c)
    def bfs(start, target):
        visited = [[-1] * col for _ in range(row)]
        q = deque([start])
        visited[start[0]][start[1]] = 0
        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r,c = q.popleft()
            if (r,c) == target:
                return visited[r][c]
            for dr, dc in moves:
                nr, nc = r+dr, c+dc
                if 0<= nr < row and 0<= nc < col:
                    if maps[nr][nc] != 'X' and visited[nr][nc] == -1:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr,nc))

        return -1

    d1 = bfs(start, lever)
    if d1 == -1:
        return -1
    d2 = bfs(lever, exit)
    if d2 == -1:
        return -1

    return d1+d2

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print(solution(maps))