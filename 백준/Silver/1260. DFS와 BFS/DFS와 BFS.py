import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 작은 번호부터 방문해야 하므로 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS
visited = [False] * (N + 1)
dfs_order = []

def dfs(v):
    visited[v] = True
    dfs_order.append(v)
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt)

dfs(V)

# BFS
visited = [False] * (N + 1)
bfs_order = []
q = deque([V])
visited[V] = True

while q:
    v = q.popleft()
    bfs_order.append(v)
    for nxt in graph[v]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)

print(*dfs_order)
print(*bfs_order)
