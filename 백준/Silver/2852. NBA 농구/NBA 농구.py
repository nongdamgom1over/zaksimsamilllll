import sys

state = 0
time_1 = 0
time_2 = 0

N = int(sys.stdin.readline().rstrip()) # 골이 들어간 횟수
for _ in range(N):
    team, time = sys.stdin.readline().split(" ")
    min, sec = map(int, time.split(":"))
    if team == "1":
        if state==0: # 첨 이긴 경우
            time_1+=48*60-(60*min+sec)
        state += 1
        if state==0: #+1후에 0인경우(2팀 이기다가 드감)
            if time_2>0:
                time_2=time_2-(48*60-(60*min+sec))
    else:
        if state==0:
            time_2+=48*60-(60*min+sec)
        state-=1
        if state==0:
            if time_1>0:
                time_1=time_1-(48*60-(60*min+sec))



print('{:0>2}:{:0>2}'.format(time_1//60, time_1%60))
print('{:0>2}:{:0>2}'.format(time_2//60, time_2%60))