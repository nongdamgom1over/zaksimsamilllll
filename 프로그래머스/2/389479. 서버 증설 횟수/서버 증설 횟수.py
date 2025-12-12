import math

def solution(players, m, k):
    answer = 0
    running = 0
    serving = {}

    for idx, player in enumerate(players):

        # 만료 처리
        if idx in serving:
            running -= serving[idx]
            del serving[idx]

        # 현재 필요 서버
        need = player // m

        # 증설 필요
        if running < need:
            add = need - running
            answer += add

            # 종료 시간에 add 만큼 끄기
            serving[idx + k] = serving.get(idx + k, 0) + add
            running += add

    return answer