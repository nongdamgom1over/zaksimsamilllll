from collections import deque
def solution(x, y, n):
    visited = [-1] * (y+1)
    visited[x] = 0

    q = deque([x]) # 먼저 들어온 것 부터 처리함 > queue
    while q:
        cur = q.popleft() # 현재가 cur
        if cur==y:
            return visited[cur]
        for nxt in (cur+n, cur*2, cur*3):
            # y를 넘으면 어차피 내려올 수 없으니 x
            if nxt <= y and visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)

    return -1 # 끝까지 봤는데 y를 못찾으면 -1리턴

x = 10
y = 40
n = 5
print(solution(x,y,n))