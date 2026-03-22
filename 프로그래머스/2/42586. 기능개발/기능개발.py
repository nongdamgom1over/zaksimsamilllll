def solution(progresses, speeds):
    answer = []
    done = []
    # 각 기능이 며칠 뒤 완료되는지 구하기
    for p,s in zip(progresses, speeds):
        d = (100 - p) / s
        if (100 - p) % s != 0:
            d+=1
        done.append(int(d))

    work = done[0]
    cnt = 1
    for day in done[1:]:
        if work >= day:
            cnt += 1
            continue
        else:
            answer.append(cnt)
            work = day
            cnt = 1
    answer.append(cnt)

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses,speeds))