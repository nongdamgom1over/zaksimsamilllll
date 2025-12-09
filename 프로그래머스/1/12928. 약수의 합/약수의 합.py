def solution(n):
    answer = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            answer+=i
            if i*i != n:
                answer+=int(n/i)
    return answer