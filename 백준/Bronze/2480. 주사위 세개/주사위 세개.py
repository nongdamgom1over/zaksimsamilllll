a, b, c = map(int,input().split(' '))
prize = 0

def solution(a,b,c):
    if (a==b==c):
        prize = 10000 + a*1000

    elif (a==b or b==c or a==c):
        if (a==b):
            prize = 1000 + a*100
        elif (b==c):
            prize = 1000 + b*100
        else:
            prize = 1000 + c*100

    else:
        d = (a,b,c)
        prize=max(d)*100

    return prize

print(solution(a,b,c))