from itertools import combinations_with_replacement as com

if __name__ == '__main__':
    n,m = map(int, input().split(" ")) # nCm 중복허용(prod)
    arr = com(range(1,n+1),m)
    for a in arr:
        print(*a)