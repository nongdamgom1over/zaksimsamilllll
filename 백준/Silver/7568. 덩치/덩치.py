import sys
N = int(sys.stdin.readline().rstrip()) # 전체 사람의 수
people = []

for _ in range(N): # N개의 줄에는 각 사람의 몸무게와 키 추가
    x,y = map(int, input().split(" "))
    people.append([x,y])

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank+=1
    print(rank, end=' ')
