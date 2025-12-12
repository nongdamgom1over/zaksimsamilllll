def solution(x):
    hashad = x
    answer = True
    num = []
    while x>=1:
        num.append(x%10)
        x //= 10
    print(num)
    if hashad % sum(num) ==0:
        answer = True
    else:
        answer = False

    return answer