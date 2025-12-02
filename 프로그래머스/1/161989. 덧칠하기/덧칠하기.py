def solution(n, m, section):
    answer = 0
    last = 0
    for part in section:
        if part > last:
            last = part + m-1
            answer += 1

    return answer