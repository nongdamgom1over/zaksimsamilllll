def solution(brown, yellow):
    answer = []
    # brown 가로길이 = yellow의 가로길이 +2 / brown 세로길이 = yellow 세로길이 +2
    for garo in range(1,yellow+1):
        if yellow % garo != 0:
            continue
        else:
            sero = yellow//garo
            if garo*2 + (sero+2)*2 == brown:
                return [max(garo + 2, sero + 2), min(garo + 2, sero + 2)]

    return answer

brown = 10
yellow = 2
print(solution(brown,yellow))