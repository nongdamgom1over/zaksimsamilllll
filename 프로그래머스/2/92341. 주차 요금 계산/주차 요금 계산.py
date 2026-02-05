import math

def solution(fees, records):
    base_t, base_fee, unit_t, unit_fee = fees

    def to_min(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    in_time = {}      # {car: 입차시각(분)}
    total_time = {}   # {car: 누적 주차시간(분)}

    for r in records:
        t, car, state = r.split()
        t = to_min(t)

        if state == "IN":
            in_time[car] = t
        else:  # OUT
            used = t - in_time.pop(car)
            total_time[car] = total_time.get(car, 0) + used

    # 아직 출차 안 한 차는 23:59에 출차 처리
    end = to_min("23:59")
    for car, t_in in in_time.items():
        used = end - t_in
        total_time[car] = total_time.get(car, 0) + used

    # 요금 계산
    answer = []
    for car in sorted(total_time.keys()):
        t = total_time[car]
        if t <= base_t:
            fee = base_fee
        else:
            extra = t - base_t
            fee = base_fee + math.ceil(extra / unit_t) * unit_fee
            # math 없이 하려면: fee = base_fee + ((extra + unit_t - 1) // unit_t) * unit_fee
        answer.append(fee)

    return answer
