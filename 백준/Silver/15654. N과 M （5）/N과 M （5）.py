from itertools import permutations

if __name__ == '__main__':
    n,m = map(int, input().split(" ")) # nCm 중복허용(prod)
    arr = list(map(int, input().split(" ")))
    arr.sort()

    for a in permutations(arr, m):
        print(*a)
