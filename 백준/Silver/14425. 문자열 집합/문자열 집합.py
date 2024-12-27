import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
s=[]
cnt = 0
for _ in range(n): # S에 포함되어야 하는 문자열들
    str = sys.stdin.readline().rstrip()
    s.append(str)

for _ in range(m):
    str = sys.stdin.readline().rstrip() # 비교할 거
    if str in s:
        cnt+=1

print(cnt)