def solution(bandage, health, attacks):
    t,x,y = bandage
    answer = health # 초기상태
    combo = 0

    last_time = attacks[-1][0] # 몬스터의 마지막 공격 시간
    idx = 0


    for time in range(1, last_time+1):
        if idx<len(attacks) and attacks[idx][0] == time: # 공격시간인지 판별
            damage = attacks[idx][1]
            answer-=damage
            combo = 0 # 콤보 초기화
            idx+=1

            if answer<=0:
                return -1

        else: # 회복하기
            combo+=1
            answer+=x
            if combo == t:
                answer+=y
                combo = 0
            if answer > health: # 최대체력인지
                answer = health

    return answer