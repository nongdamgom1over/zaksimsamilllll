def solution(number):
    answer = 0
    n = len(number)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for r in range(j+1,n):
                if number[i]+number[j]+number[r] == 0 :
                    answer+=1
    return answer
