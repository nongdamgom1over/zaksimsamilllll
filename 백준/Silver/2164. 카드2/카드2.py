import sys

N = int(sys.stdin.readline().rstrip())
queue = []
first = 0
last = N-1
res = 0

for i in range(1,N+1,1):
    queue.append(i)

state = 0 # 0=버리기 1=쌓기
while True:
    if len(queue)-first==1:
        res = queue[first]
        break
    elif state==0:
        first+=1
        state=1
    elif state==1:
        queue.append(queue[first])
        first+=1
        last+=1
        state=0

print(res)

