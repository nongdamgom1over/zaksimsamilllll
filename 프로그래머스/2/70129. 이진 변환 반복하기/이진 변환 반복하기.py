import math
def solution(s):
    binary = 0
    zero = 0

    while s!='1':
        st = ''
        for i in range(len(s)): # 0 제거
            if s[i]=='1':
                st+=s[i]
            else:
                zero+=1
        c = len(st)
        s = bin(c)[2:]
        binary+=1

    return [binary,zero]

s = "110010101001"
print(solution(s))