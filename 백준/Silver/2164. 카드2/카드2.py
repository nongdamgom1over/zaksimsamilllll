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
    if len(queue)-first == 1:
        res = queue[first] # 마지막 남아있는거 쳐 저장하고
        break
    elif state==0: # 버리기
        first+=1
        state=1
    elif state==1: #쌓기
        queue.append(queue[first])
        first+=1
        last+=1
        state=0


print(res)

