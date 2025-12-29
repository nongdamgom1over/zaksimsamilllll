from collections import deque
def solution(board):
    n, m = len(board), len(board[0])
    board = [list(row) for row in board]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i,j)

    visited = [[-1] * m for _ in range(n)]
    q = deque([start])
    visited[start[0]][start[1]] = 0

    direction = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        r,c = q.popleft()

        if board[r][c] == 'G':
            return visited[r][c]

        for dr, dc in direction:
            nr, nc = r, c
            while True:
                tr, tc = nr+dr, nc+dc
                if not (0<=tr<n and 0<=tc<m):
                    break
                if board[tr][tc] == 'D':
                    break
                nr,nc = tr,tc
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr,nc))

    return -1

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))