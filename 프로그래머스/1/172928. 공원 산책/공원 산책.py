def solution(park, routes):
    answer = []
    w = len(park[0])
    h = len(park)

    # 1) S 위치
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                y, x = i, j

    # 2) 방향 벡터 정의
    move = {
        'E' : (0,1),
        'W' : (0, -1),
        'N' : (-1,0),
        'S' : (1, 0)
    }

    # 3) 명령 처리
    for route in routes:
        op, dist = route.split()
        dist = int(dist)

        dy, dx = move[op]

        ny, nx = y,x
        ok = True

        # 경로 유효성 체크
        for _ in range(dist):
            ny += dy
            nx += dx

            if ny < 0 or ny >= h or nx<0 or nx>= w:
                ok = False
                break

            if park[ny][nx] == 'X':
                ok = False
                break

        if ok == True:
            y,x = ny, nx
    answer.append(y)
    answer.append(x)

    return answer