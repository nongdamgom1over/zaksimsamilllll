def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(time):
        mm, ss = map(int, time.split(":"))
        return mm * 60 + ss

    now = to_sec(pos)
    v_len = to_sec(video_len)
    op_s = to_sec(op_start)
    op_e = to_sec(op_end)

    # 시작 시점 오프닝 체크
    if op_s <= now <= op_e:
        now = op_e

    for cmd in commands:
        if cmd == "prev":
            now -= 10
        else:  # next
            now += 10

        # 1) 영상 범위 보정
        now = max(0, min(now, v_len))

        # 2) 오프닝 구간 보정
        if op_s <= now <= op_e:
            now = op_e

    m = now // 60
    s = now % 60
    
    answer = f"{m:02d}:{s:02d}"
    return answer
