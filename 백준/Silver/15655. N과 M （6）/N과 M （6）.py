from itertools import combinations

if __name__ == '__main__':
    n,m = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    arr.sort()

    for a in combinations(arr,m):
        print(*a)
