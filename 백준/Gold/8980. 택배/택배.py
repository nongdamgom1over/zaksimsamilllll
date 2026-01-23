def solution(N,C,delivery):
    # 1) 도착지(받는 마을) 기준 오름차순 정렬 (가까운 곳 먼저 내려서 공간 확보)
    delivery.sort(key=lambda x: (x[1], x[0]))

    # 2) 각 구간 i -> i+1 에서 남은 적재 가능 용량
    #    remain[i]는 i->i+1 구간의 남은 용량 (1..N-1 사용)
    remain = [C] * (N + 1) # 초기엔 남은 적재용량 모두 C

    ans = 0
    for s, d, box in delivery:
        # 3) 이 배송이 지나가는 구간들(s..d-1) 중 최소 남은 용량이 실을 수 있는 최대치
        can = box
        for i in range(s, d):
            if remain[i] < can: # 남은 적재용량<가능용량
                can = remain[i]

        # 4) 그만큼 실어서 각 구간 용량에서 차감
        if can > 0:
            for i in range(s, d):
                remain[i] -= can
            ans += can #

    return ans

N, C = map(int, input().split(" ")) # N : 마을의 수 C : 트럭용량
M = int(input())
delivery = []
for _ in range(M):
    s,d,i = map(int,input().split(" "))
    delivery.append([s,d,i]) # 시작 목적지 택배수

print(solution(N,C,delivery))