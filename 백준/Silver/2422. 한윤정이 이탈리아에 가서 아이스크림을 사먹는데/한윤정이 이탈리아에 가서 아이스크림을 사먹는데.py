from itertools import combinations
import math

if __name__ == '__main__':
    n,m = map(int, input().split(" "))
    kirai = set()
    for _ in range(m):
        a, b = map(int, input().split(" "))
        kirai.add((a,b))
        kirai.add((b,a))

    res = 0
    for a,b,c in combinations(range(1,n+1), 3):
        if (a,b) in kirai or (a,c) in kirai or (b,c) in kirai:
            continue
        res+=1

    print(res)