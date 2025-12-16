from collections import defaultdict

def solution(points, routes):
    # 포인트 번호 → 좌표
    pos = {i+1: tuple(points[i]) for i in range(len(points))}
    
    # 로봇별 이동 경로 (초 단위 좌표 리스트)
    paths = []

    for route in routes:
        path = []
        cur_r, cur_c = pos[route[0]]
        path.append((cur_r, cur_c))

        for i in range(1, len(route)):
            tr, tc = pos[route[i]]

            # r 먼저 이동
            while cur_r != tr:
                cur_r += 1 if tr > cur_r else -1
                path.append((cur_r, cur_c))

            # c 이동
            while cur_c != tc:
                cur_c += 1 if tc > cur_c else -1
                path.append((cur_r, cur_c))

        paths.append(path)

    # 전체 시뮬레이션 시간
    max_time = max(len(p) for p in paths)

    danger = 0

    # 시간별 충돌 체크
    for t in range(max_time):
        counter = defaultdict(int)
        for path in paths:
            if t < len(path):
                counter[path[t]] += 1

        for cnt in counter.values():
            if cnt >= 2:
                danger += 1

    return danger
