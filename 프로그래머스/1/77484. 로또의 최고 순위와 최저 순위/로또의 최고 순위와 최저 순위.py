def solution(lottos, win_nums):
    answer = []
    cnt_0 = 0 # 0개의 갯수
    cnt_win = 0 # 당첨 번호 갯수

    # 1. 0이 아닌 것 중에 당첨 번호랑 맞는 거 갯수 / 0인거 갯수
    for lotto in lottos:
        if lotto == 0: # 알아보지 못하는 번호인 경우
            cnt_0 += 1
        elif lotto in win_nums: # 당첨 번호에 해당 하는 경우
            cnt_win += 1

    # 2. cnt_0 + cnt_win 가 최대 순위
    #answer += "R" if scores["R"] >= scores["T"] else "T"
    if cnt_0 + cnt_win == 6:
        answer.append(1)
    elif cnt_0 + cnt_win == 5:
        answer.append(2)
    elif cnt_0 + cnt_win == 4:
        answer.append(3)
    elif cnt_0 + cnt_win == 3:
        answer.append(4)
    elif cnt_0 + cnt_win == 2:
        answer.append(5)
    else:
        answer.append(6)

    # 3. cnt_win이 최소 순위
    if cnt_win == 6:
        answer.append(1)
    elif cnt_win == 5:
        answer.append(2)
    elif cnt_win == 4:
        answer.append(3)
    elif cnt_win == 3:
        answer.append(4)
    elif cnt_win == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer