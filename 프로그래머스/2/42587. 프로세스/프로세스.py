from collections import deque
def solution(priorities, location):
    q = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0

    while q:
        idx, priority = q.popleft()

        if any(priority < p for _, p in q):
            q.append((idx, priority))
        else:
            count += 1
            if idx == location:
                return count

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities,location))