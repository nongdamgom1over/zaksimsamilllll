def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)

    # 1) 여벌도 있었는데 도난당한 학생 처리
    real_lost = []
    real_reserve = []

    for l in lost:
        if l not in reserve:
            real_lost.append(l)
        else:
            reserve.remove(l)  # 자기 것만 입고 빌려주는 리스트에서는 제거

    reserve = reserve  # 반영
    lost = real_lost

    # 2) 빌려줄 수 있는 학생이 있는지 확인
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    # 3) 가능한 학생 수
    return n - len(lost)
