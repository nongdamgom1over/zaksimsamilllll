def solution(s):
    answer = 0

    state = False
    x = ''
    for ch in s:
        if x == '':
            x = ch
            x_cnt, not_x_cnt = 1, 0


        else:
            if ch == x:
                x_cnt += 1
            else:
                not_x_cnt += 1

        if x_cnt == not_x_cnt:
            answer+=1
            x = ''

    # 마지막 덩이 비지 않은 경우
    if x != '':
        answer += 1

    return answer

s = "abracadabra"
print(solution(s))