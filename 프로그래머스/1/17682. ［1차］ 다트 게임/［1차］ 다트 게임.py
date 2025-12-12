def solution(dartResult):
    scores = []
    num = ""

    for ch in dartResult:
        if ch.isdigit(): # 숫자면
            num += ch
        elif ch in "SDT": # SDT중 하나면
            n = int(num)
            if ch == "S":
                n = n**1
            elif ch == "D":
                n = n**2
            elif ch == "T":
                n = n**3
            scores.append(n)
            num = ""
        elif ch == "*":
            scores[-1] *= 2 # 현재 점수 2배
            # 이전 점수도 있으면
            if len(scores) > 1:
                scores[-2] *= 2
        elif ch == "#":
            scores[-1] *= -1

    return sum(scores)

dartResult = "1S2D*3T"
print(solution(dartResult))