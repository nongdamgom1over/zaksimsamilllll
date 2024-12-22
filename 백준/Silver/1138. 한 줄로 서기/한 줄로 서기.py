import sys

n = int(sys.stdin.readline().rstrip())
memory = list(map(int,sys.stdin.readline().rstrip().split(" ")))

line = [0]*n # 다 0으로 초기화

for i in range(n):
    cnt = 0
    for j in range(n):
        if line[j] == 0:
            cnt+=1
        if memory[i]+1 == cnt:
            line[j] = i + 1
            break

print(*line)