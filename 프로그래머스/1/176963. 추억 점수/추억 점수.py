def solution(name, yearning, photo):
    answer = []
    n = len(name)

    # 1. name과 yearning value 매핑
    score = {}
    for i in range(n):
        score[name[i]] = yearning[i]
    # 딕셔너리 컴프리헨션 : score = {name[i]: yearning[i] for i in range(n)}

    # 2: 각 photo의 사람들 이름 보고 점수 합산
    for people in photo:
        total = 0
        for person in people:
            total += score.get(person, 0) # 없으면 0
        answer.append(total)

    return answer