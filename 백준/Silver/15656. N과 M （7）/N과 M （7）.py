from itertools import product

if __name__ == '__main__':
    n,m = map(int, input().split(" ")) # nCm 중복허용(prod)
    arr = list(map(int, input().split(" ")))
    arr.sort()
    prod = product(arr,repeat=m)
    for p in prod:
        print(*p)
