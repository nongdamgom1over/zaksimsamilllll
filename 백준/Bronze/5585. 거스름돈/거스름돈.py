def solution(amount):
    answer = 0
    bills = [500,100,50,10,5,1]
    charge = 1000-amount
    while charge>0:
        for b in bills:
            if charge >= b:
                answer += charge//b
                charge = charge % b
            else:
                continue
    return answer

amount = int(input())
print(solution(amount))