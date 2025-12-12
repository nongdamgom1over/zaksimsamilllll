def solution(info, n, m):
    items = len(info) # 총 훔쳐야할 물건 갯수

    dp = [[[False] * (m+1) for _ in range(n+1)] for _ in range(items +1)]
    dp[0][0][0] = True # 시작점만 true

    for i in range(items):
        a_trace, b_trace = info[i]
        for a in range(n):
            for b in range(m):
                if not dp[i][a][b]:
                    continue
                # i물건을 A가 훔치는 경우
                na = a + a_trace # a의 새 흔적
                nb = b
                if na < n:
                    dp[i+1][na][nb] = True

                # i물건 B가 훔치는 경우
                na = a
                nb = b + b_trace
                if nb < m:
                    dp[i+1][na][nb] = True

    answer = float("inf")
    for a in range(n):
        for b in range(m):
            if dp[items][a][b]:
                answer = min(answer, a)


    return answer if answer != float("inf") else -1

info = [[1, 2], [2, 3], [2, 1]]
n = 4
m = 4
print(solution(info,n,m))