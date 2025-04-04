from itertools import combinations

if __name__ == '__main__':
    n, m = map(int, input().split(" "))
    nums = [i for i in range(1,n+1)]
    arr = combinations(nums, m)

    for word in arr:
        print(" ".join(map(str,word)))