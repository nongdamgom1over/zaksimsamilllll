import sys
H, W = map(int, input().split(" "))
cloud = []
for i in range(H):
    cloud.append([])
    w = input()
    for j in w:
        cloud[i].append(j)


for i in range(H):
    c = -1
    for j in range(W):
        if j==0:
            if cloud[i][j] == 'c':
                c = 0
                print(0, end=' ')
            else:
                print(-1, end=' ')
        else:
            if cloud[i][j] == 'c':
                c = j
                print(0, end=' ')
            elif c != -1:
                print(j-c, end=' ')
            else:
                print(-1, end=' ')
    print()

