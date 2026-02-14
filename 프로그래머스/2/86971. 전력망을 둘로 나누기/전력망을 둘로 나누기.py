from collections import deque
def solution(n, wires):
    answer = float('inf')
    # 1) 그래프 그리기
    adj = [[] for _ in range(n+1)]
    for u,v in wires:
        adj[u].append(v)
        adj[v].append(u)

    def bfs_count(start, cut_u, cut_v):
        q = deque([start])
        visited = [False] * (n+1)
        visited[start] = True
        cnt = 1

        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                # 2) 끊은 간선 스킵
                if (cur == cut_u and nxt == cut_v) or (nxt == cut_u and cur == cut_v):
                    continue
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    cnt += 1
        return cnt

    for a,b in wires:
        k = bfs_count(a,a,b)
        diff = abs(n-2*k) # 끊고 나면 k / n-k
        answer = min(answer, diff)

    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))