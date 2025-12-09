def solution(left, right):
    answer = 0
    def yaksu(num):
        cnt = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:  # i가 약수라면
                cnt += 1
                if i != num // i:  # i와 짝이 다르면 (완전제곱수 아니면)
                    cnt += 1  # 짝인 약수까지 추가
        return cnt

    for j in range(left, right+1):
        if yaksu(j)%2 == 0:
            answer+=j
        else:
            answer-=j

    return answer