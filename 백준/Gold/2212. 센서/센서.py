def solution(N,K,cord):
    # 좌표들 정렬
    cord = sorted(set(cord))
    # 좌표간 간격 계산
    arr = []
    for i in range(1,len(cord)):
        n = cord[i] - cord[i-1]
        arr.append(n)
    arr.sort(reverse=True)

    return sum(arr[K-1:])

N = int(input())
K = int(input())
cord = list(map(int, input().split(" ")))
print(solution(N,K,cord))