from itertools import permutations



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split(" "))

    data = list(permutations(arr,n))

    res = 0  # sum
    for i in range(len(data)):
        hap = 0
        for j in range(1,n):
            if data[i][j] >= data[i][j-1]:
                hap += data[i][j]-data[i][j-1]
            else:
                hap += data[i][j-1]-data[i][j]

        if hap > res:
            res = hap

    print(res)