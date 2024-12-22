import sys

def gcd(a,b):
    r=0
    while (b!=0):
        r = a%b
        a=b
        b=r
    return a

def lcm(a,b):
    res = (a*b)/gcd(a,b)
    return res

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    print("%i" %lcm(a,b))

