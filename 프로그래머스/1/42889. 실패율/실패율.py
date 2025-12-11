def solution(N, stages):
    user = len(stages) # 전체 유저 수
    count = {i: 0 for i in range(1,N+2)} # key : 스테이지번호, value : 실패율
    for stage in stages:
        count[stage] += 1

    fail = []
    for stage in range(1, N+1):
        if user == 0:
            fail_rate = 0
        else:
            fail_rate = count[stage] / user

        fail.append((stage,fail_rate))
        user -= count[stage]

    # 실패율 내림차순, 같으면 stage 오름차순
    fail.sort(key=lambda x: (-x[1], x[0]))

    # stage만 추출
    return [stage for stage, rate in fail]

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))