def solution(arr):
    n = len(arr)
    zero, one = 0, 0

    def compress(x,y,size):
        nonlocal zero,one
        for i in range(size):
            for j in range(size):
                if arr[x+i][y+j] != arr[x][y]:
                    # 다시 4등분
                    half = size // 2
                    compress(x,y,half)
                    compress(x+half,y,half)
                    compress(x,y+half,half)
                    compress(x+half,y+half,half)
                    return 
        # 균일
        if arr[x][y] == 0:
            zero+=1
        else:
            one+=1

    compress(0, 0, n)
    return [zero, one]

arr = [[1,1,1,1,1,1,1,1],
       [0,1,1,1,1,1,1,1],
       [0,0,0,0,1,1,1,1],
       [0,1,0,0,1,1,1,1],
       [0,0,0,0,0,0,1,1],
       [0,0,0,0,0,0,0,1],
       [0,0,0,0,1,0,0,1],
       [0,0,0,0,1,1,1,1]]
print(solution(arr))