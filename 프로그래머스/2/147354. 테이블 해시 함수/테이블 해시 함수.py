# XOR 다르면 1, 같으면 0 ex x^0=x/x^x=0
def solution(data, col, row_begin, row_end):
    answer = 0
    db = sorted(data, key=lambda x: (x[col-1], -x[0]))
    n = len(data[0])
    for i in range(row_begin-1, row_end):
        num = 0
        for j in range(n):
            num+=(db[i][j] % (i+1))
        answer^=num

    return answer

data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3
print(solution(data,col,row_begin,row_end))