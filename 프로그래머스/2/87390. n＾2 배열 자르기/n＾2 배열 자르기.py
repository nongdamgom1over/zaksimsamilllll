def solution(n, left, right):
    answer = []
    for idx in range(left, right + 1):
        r = idx // n
        c = idx % n
        answer.append(max(r, c) + 1)
    return answer

print(solution(3, 2, 5))  # [3, 2, 2, 3]
