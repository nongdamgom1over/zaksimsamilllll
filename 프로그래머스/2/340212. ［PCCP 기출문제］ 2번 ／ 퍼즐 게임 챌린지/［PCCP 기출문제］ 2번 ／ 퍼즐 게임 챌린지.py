def solution(diffs, times, limit):
    answer = 0
    left = 1
    right = max(diffs)

    def cal_time(level, diffs, times, limit):
        time = 0 # 총 소요 시간
        time_prev = 0

        for i in range(len(diffs)):
            if diffs[i] <= level:
                time += times[i]
            else:
                time += ((times[i] + time_prev) * (diffs[i] - level) + times[i])

            if time > limit:
                return False

            time_prev = times[i]

        return True

    while left <= right:
        mid = (left+right)//2
        if cal_time(mid, diffs, times, limit):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer