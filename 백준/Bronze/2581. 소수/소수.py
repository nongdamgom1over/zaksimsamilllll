import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
prime = []

def isPrimeNum(num):
    if num < 2:
        return False
    for i in range(2,num):
        if (num % i == 0):
            return False
    return True

for i in range(M,N+1,1):
    if (isPrimeNum(i) == True):
        prime.append(i)

if (len(prime) == 0):
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
