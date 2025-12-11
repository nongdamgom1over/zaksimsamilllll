def solution(board, moves):
    answer = 0
    stack = [] # 바구니
    n = len(board)
    for move in moves:
        for i in range(n):
            if board[i][move-1] != 0:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                break

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            answer+=2
            stack.pop()
            stack.pop()

    return answer