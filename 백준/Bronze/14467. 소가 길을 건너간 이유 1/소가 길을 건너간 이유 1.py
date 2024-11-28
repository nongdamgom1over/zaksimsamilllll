import sys

N = int(sys.stdin.readline().rstrip())
dic = dict()
cnt = 0

for i in range(N):
     a, b = map(int, input().split(" "))
     if a in dic:
         if dic[a] != b:
             cnt += 1
             dic[a] = b
     else:
         dic[a] = b

print(cnt)

