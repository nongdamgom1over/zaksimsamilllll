import math

def solution(n, r):
    res = math.comb(n,r)
    return res

if __name__ == '__main__':
    n, r = map(int, input().split())
    res = solution(n, r)
    print(res)
