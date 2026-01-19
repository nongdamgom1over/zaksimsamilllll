def solution(k, ranges):
    answer = []
    arr = [] # 좌표
    x = 0
    while k>1:
        arr.append((x,k))
        x+=1
        if k%2 == 0: # 짝수
            k=k//2
        else: # 호수
            k = k*3 + 1
    arr.append((x,k))
    # 정적분 구하기
    # y값만 뽑기 (arr은 (x,y)니까)
    y = [val for _, val in arr]
    n = len(y) - 1  # 우박수열이 1될 때까지 횟수 (x의 마지막 값)

    # 1) 각 구간(폭 1)의 사다리꼴 넓이
    area = []
    for i in range(n):
        area.append((y[i] + y[i+1]) / 2)

    # 2) 누적합 prefix 만들기
    prefix = [0.0] * (n + 1)  # prefix[t] = 0~t-1 구간 넓이 합
    for i in range(n):
        prefix[i+1] = prefix[i] + area[i]

    # 3) ranges 처리
    for a, b in ranges:
        end = n + b  # b는 0 또는 음수
        if a > end:
            answer.append(-1.0)
        else:
            answer.append(prefix[end] - prefix[a])


    return answer

k = 5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]
print(solution(k,ranges))