T = int(input())
for _ in range(T):
    N = int(input())
    cycle = [0] + list(map(int, input().split(" ")))
    cnt = 0
    visited = [False] * (N+1)
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        cur = i
        while not visited[cur]:
            visited[cur] = True
            cur = cycle[cur]
        cnt+=1
    
    print(cnt)
