from itertools import permutations



if __name__ == '__main__':
    n, m = map(int, input().split(" "))
    nums = [i for i in range(1,n+1)]
    arr = permutations(nums, m)

    for comb in arr:
        print(" ".join(map(str, comb)))