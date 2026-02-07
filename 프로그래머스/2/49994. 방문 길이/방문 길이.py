def solution(dirs):
    answer = 0
    command = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    x,y = 0,0
    visited = set()

    for ch in dirs:
        dx, dy = command[ch]
        nx,ny = x+dx, y+dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = (x, y, nx, ny)
            rev = (nx, ny, x, y)
            if path not in visited:
                visited.add(path)
                visited.add(rev)
                answer += 1
            x, y = nx, ny

    return answer

dirs = "LULLLLLLU"
print(solution(dirs))