def solution(mats, park):
    answer = 0
    rows = len(park)
    cols = len(park[0])
    mats.sort(reverse=True) # 큰 것 부터 탐색

    # k * k 영역이 전부 -1 인지 확인
    def is_empty(i,j,k):
        if i+k > rows or j+k > cols: # 공원 크기를 벗어나는지
            return False
        for r in range(i,i+k):
            for c in range(j,j+k):
                if park[r][c] != '-1':
                    return False
        return True

    for k in mats:
        for i in range(rows):
            for j in range(cols):
                if is_empty(i,j,k):
                    answer = k
                    return answer

    return -1