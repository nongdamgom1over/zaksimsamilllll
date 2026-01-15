def solution(storey):
    answer = 0
    while storey>0:
        digit = storey % 10
        next_digit = (storey // 10) % 10

        if digit > 5: # 5보다 크면 층 올라가는게 빠름
            answer += (10 - digit)
            storey+=10
        elif digit<5 : # 내려가기
            answer += digit
        else: # digit == 5
            # 다음 자리가 5이상이면 올림, 아니면 내림
            if next_digit >= 5:
                answer+=5
                storey+=10
            else:
                answer+=5

        storey //= 10
    return answer

storey = 2554
print(solution(storey))