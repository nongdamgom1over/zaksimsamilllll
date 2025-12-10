def solution(survey, choices):
    # 1) 점수판 초기화
    scores = { 'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0 }

    for s, c in zip(survey, choices):
        disagree = s[0]  # 비동의시 점수 받는 성격
        agree = s[1]     # 동의시 점수 받는 성격
        
        if c < 4:   # 비동의 계열
            scores[disagree] += (4 - c)
        elif c > 4: # 동의 계열
            scores[agree] += (c - 4)
        # choice == 4면 0점이므로 아무 것도 안 함

    # 4개 지표 비교
    answer = ""
    answer += "R" if scores['R'] >= scores['T'] else "T"
    answer += "C" if scores['C'] >= scores['F'] else "F"
    answer += "J" if scores['J'] >= scores['M'] else "M"
    answer += "A" if scores['A'] >= scores['N'] else "N"

    return answer
