import math
def solution(n, k):
    answer = 0

    def to_base(num,base):
        s = ''
        while num>0:
            num,mod = divmod(num,base)
            s = str(mod) + s
        return s

    def is_prime(num):
        if num<2:
            return False
        if num==2:
            return True
        if num%2 == 0:
            return False
        r = int(math.isqrt(num))
        for i in range(3,r+1,2):
            if num%i==0:
                return False
        return True

    n = to_base(n,k)
    temp = ''
    for ch in n:
        if ch == '0':
            if temp and is_prime(int(temp)):
                answer+=1
            temp = ''
        else:
            temp+=ch
    if temp and is_prime(int(temp)):
        answer+=1

    return answer

n = 437674
k = 3
print(solution(n,k))