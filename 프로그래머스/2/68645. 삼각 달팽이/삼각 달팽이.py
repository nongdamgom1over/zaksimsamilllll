def solution(n):
    answer = []
    # 초기 2차원 배열
    triangle = [[0] * (i+1) for i in range(n)]
    # 시작지정
    x,y = -1,0
    num = 1
    for step in range(n,0,-1): # step : 4>3>2>1
        dir = (n-step) % 3 # 방향 선택 아래>옆>위>아래
        for _ in range(step):
            if dir == 0: # 아래
                x+=1
            elif dir == 1: # 옆
                y+=1
            else:
                x-=1
                y-=1

            triangle[x][y] = num
            num+=1

    # answer 도출
    for row in triangle:
        answer.extend(row)
        # 리스트에 다른 리스트(또는 iterable)의 원소들을 하나씩 풀어서 추가하는 함수

    return answer

n = 6
print(solution(n))