def solution(rows, columns, queries):
    answer = []
    arr = [[0]*columns for _ in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = n
            n+=1
    for x1,y1,x2,y2 in queries:
        x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
        temp = arr[x1][y1]
        min_val = temp
        for x in range(x1,x2):
            min_val = min(min_val, arr[x+1][y1])
            arr[x][y1] = arr[x+1][y1]
        for y in range(y1, y2):
            min_val = min(min_val, arr[x2][y+1])
            arr[x2][y] = arr[x2][y+1]
        for x in range(x2,x1,-1):
            min_val = min(min_val, arr[x-1][y2])
            arr[x][y2] = arr[x-1][y2]
        for y in range(y2,y1,-1):
            min_val = min(min_val, arr[x1][y-1])
            arr[x1][y] = arr[x1][y-1]
        arr[x1][y1+1] = temp
        answer.append(min_val)

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows,columns,queries))