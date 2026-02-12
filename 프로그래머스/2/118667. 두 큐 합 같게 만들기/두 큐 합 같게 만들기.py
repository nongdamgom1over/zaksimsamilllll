from collections import deque

def solution(queue1, queue2):
    n = len(queue1)
    s1 = sum(queue1)
    s2 = sum(queue2)
    total = s1 + s2

    if total % 2 == 1:
        return -1
    target = total // 2

    q1 = deque(queue1)
    q2 = deque(queue2)

    # 최대 이동 횟수 상한 (관례적으로 3*n이면 충분)
    # (queue1에서 최대 2n번 빠지고, queue2에서 최대 2n번 들어오고…)
    limit = 3 * n
    ops = 0

    while ops <= limit:
        if s1 == target:
            return ops

        if s1 > target:
            if not q1:
                return -1
            x = q1.popleft()
            s1 -= x
            q2.append(x)
        else:  # s1 < target
            if not q2:
                return -1
            x = q2.popleft()
            s1 += x
            q1.append(x)

        ops += 1

    return -1
