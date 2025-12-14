from itertools import combinations

def solution(n, q, ans):
    answer = 0
    q = [set(query) for query in q]
    for ans_can in combinations(range(1,n+1),5):
        card = set(ans_can)
        ok = True
        for i in range(len(q)):
            if len(card & q[i]) != ans[i]:
                ok = False
                break
        if ok == True:
            answer += 1

    return answer

n = 10
q = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]]
ans = [2, 3, 4, 3, 3]
print(solution(n,q,ans))