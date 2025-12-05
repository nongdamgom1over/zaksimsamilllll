def solution(number, limit, power):
    answer = 0
    people = []

    def yaksu(num):
        cnt = 0
        i = 1
        while i*i<= num:
            if num % i == 0:
                cnt+=1
                if i * i != num:
                    cnt+=1
            i += 1
        return cnt

    for i in range(1,number+1):
        num = yaksu(i)
        if num > limit:
            num = power
        people.append(num)

    answer = sum(people)

    return answer