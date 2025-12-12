def solution(answers):
    answer = []

    # 점수 딕셔너리 초기화
    score = {x: 0 for x in range(1, 4)}

    # 각 수포자의 패턴 (리스트로 변경)
    pattern = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    for idx, ans in enumerate(answers):
        # 1번 수포자
        if ans == pattern[0][idx % len(pattern[0])]:
            score[1] += 1
        # 2번 수포자
        if ans == pattern[1][idx % len(pattern[1])]:
            score[2] += 1
        # 3번 수포자
        if ans == pattern[2][idx % len(pattern[2])]:
            score[3] += 1

    # 최고 점수 찾기
    max_score = max(score.values())

    # 최고 점수를 받은 사람들만 answer에 추가 (번호 오름차순 자동 보장)
    for person, s in score.items():
        if s == max_score:
            answer.append(person)

    return answer