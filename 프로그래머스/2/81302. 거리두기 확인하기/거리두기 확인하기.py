def solution(places):
    answer = []
    for place in places:
        arr = [list(row) for row in place]
        ok = 1
        for r in range(5):
            for c in range(5):
                if arr[r][c] == 'P': # 인간이 있으면
                    # 거리 1 검사
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        if 0<=r+dx and r+dx<5 and 0<=c+dy and c+dy<5:
                            if arr[r+dx][c+dy] == 'P':
                                ok = 0

                    if ok == 0:
                        break

                    # 거리 2 직선 검사
                    for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
                        if 0 <= r + dx and r + dx < 5 and 0 <= c + dy and c + dy < 5:
                            if arr[r + dx][c + dy] == 'P':
                                mid_r = r + dx // 2
                                mid_c = c + dy // 2
                                if arr[mid_r][mid_c] != 'X':
                                    ok = 0
                    if ok == 0:
                        break

                    # 대각선
                    for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                        if 0 <= r + dx and r + dx < 5 and 0 <= c + dy and c + dy < 5:
                            if arr[r + dx][c + dy] == 'P':
                                if arr[r + dx][c] != 'X' or arr[r][c + dy] != 'X':
                                    ok = 0
                    if ok == 0:
                        break


        answer.append(ok)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))