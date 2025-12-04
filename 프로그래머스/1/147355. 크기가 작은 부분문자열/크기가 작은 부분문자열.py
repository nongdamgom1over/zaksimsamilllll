def solution(t, p):
    answer = 0
    n = len(p)

    for i in range(len(t)-n+1):
        word = ''
        for j in range(i,i+n):
            word += t[j]
        if int(word) <= int(p):
            answer+=1

    return answer