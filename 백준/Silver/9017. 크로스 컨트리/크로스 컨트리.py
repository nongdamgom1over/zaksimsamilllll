import sys

T = int(sys.stdin.readline().rstrip()) # T개의 테스트 케이스
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    res = list(map(int, sys.stdin.readline().split(" ")))

    team = {}
    for i in range(N):
        if res[i] not in team:
            team[res[i]] = [1, [], 0] # 팀의 인원 수, 팀의 점수 리스트, 점수합
        else:
            team[res[i]][0] += 1

    elim = set(k for k, v in team.items() if v[0]<6)

    rank = 1
    for i in range(N):
        if res[i] not in elim:
            team[res[i]][1].append(rank)
            if len(team[res[i]][1]) <= 4:
                team[res[i]][2] += rank
            rank += 1




    ans = []
    for k,v in team.items():
        if len(v[1]) != 0 and v[2] != 0:
            ans.append([k, v[1][4], v[2]])
    a = sorted(ans, key=lambda x: (x[2], x[1])) # x[2] = v[2], x[1] = v[1][4]

    print(a[0][0])
