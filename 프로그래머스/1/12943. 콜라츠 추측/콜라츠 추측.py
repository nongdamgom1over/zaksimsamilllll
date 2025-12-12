def solution(num):
    answer = 0
    while num > 1:
        # 1-1. 입력된 수가 짝수라면 2로 나눕니다.
        if num % 2 == 0:
            num //= 2
        # 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
        elif num % 2 == 1:
            num = num*3 + 1
        answer += 1
        if answer > 500:
            return -1

    return answer

n = 6
print(solution(n))