def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)

    # 각 이벤트 날짜의 요일 계산 (1~7)
    weekdays = []
    for x in range(7):
        weekdays.append((startday - 1 + x) % 7 + 1)

    for i in range(n):
        hope = schedules[i]

        # +10분 계산
        h = hope // 100
        m = hope % 100
        m += 10
        if m >= 60:
            m -= 60
            h += 1
        deadline = h * 100 + m

        flag = 1  # 직원별 확인 시작

        for day_idx in range(7):   # 0~6
            if 1 <= weekdays[day_idx] <= 5:  # 평일만
                if timelogs[i][day_idx] > deadline:
                    flag = 0
                    break

        if flag == 1:
            answer += 1

    return answer
