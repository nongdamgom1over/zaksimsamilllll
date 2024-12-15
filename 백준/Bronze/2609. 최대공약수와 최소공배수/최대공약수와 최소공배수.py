import sys

def yaksu(a,b):
    while (b>0):
        res = a%b
        a=b
        b=res
    return a

def baesu(a,b):
    return a*b//yaksu(a,b)


a,b = map(int, sys.stdin.readline().split(" "))

print(yaksu(a,b))
print(int(baesu(a,b)))