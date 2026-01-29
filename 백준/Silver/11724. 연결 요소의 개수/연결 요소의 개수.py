import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        v = stack.pop()
        for nxt in adj[v]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N + 1)
answer = 0

for v in range(1, N + 1):
    if not visited[v]:
        dfs(v)
        answer += 1

print(answer)
