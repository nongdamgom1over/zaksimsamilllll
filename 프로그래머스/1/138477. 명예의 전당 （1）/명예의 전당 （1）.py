
def solution(k, score):
    answer = []
    award = [] # 명예의 전당
    for idx, s in enumerate(score):
        award.append(s)
        award.sort()
        if idx < k:
            answer.append(award[0])
        else:
            answer.append(award[-k])

    return answer