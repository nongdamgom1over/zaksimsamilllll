from itertools import combinations

if __name__ == '__main__':
    while True:
        S = list(map(int, input().split(" ")))
        if S[0] == 0:
            break
        k = S[0]
        nums = S[1:]

        for num in combinations(nums,6):
            print(*num)
        print()