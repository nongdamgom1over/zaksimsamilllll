import math
def solution(n):
    i = n+1 # i를 높힐거긔
    to_bin = bin(n)
    num = 0
    for ch in range(len(str(to_bin))):
        if to_bin[ch] == "1":
            num+=1
    while True:
        i_bin = bin(i)
        i_num = 0
        for ch in range(len(str(i_bin))):
            if i_bin[ch] == "1":
                i_num += 1
        if i_num == num:
            break
        i+=1
    return i
n = 78
print(solution(n))