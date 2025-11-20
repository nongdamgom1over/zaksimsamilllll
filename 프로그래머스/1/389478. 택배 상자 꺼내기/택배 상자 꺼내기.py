def solution(n, w, num):
    answer = 0
    a = w
    b = n // w + 1

    arr = [[] for _ in range(a)]  # 열 기준으로 arr[col][row] 형태

    box = 1
    num_row, num_col = 0, 0

    for i in range(b):
        if i % 2 == 0:  # 짝수 행: 왼 → 오
            rng = range(a)
        else:  # 홀수 행: 오 → 왼
            rng = reversed(range(a))

        for col in rng:
            if box > n:
                break
            arr[col].append(box)
            if box == num:
                num_col = col
                num_row = len(arr[col]) - 1
            box += 1

    # 아래에서부터 위로: 위에 있는 박스는 리스트의 뒤쪽 요소
    answer = len(arr[num_col]) - num_row

    return answer