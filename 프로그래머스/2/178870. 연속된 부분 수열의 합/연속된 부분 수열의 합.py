def solution(sequence, k):
    n = len(sequence)
    left = 0
    sum = 0 # 구간합

    best_len = float('inf')
    best = [0, 0]

    for right in range(n):
        sum += sequence[right]

        while sum > k and left <= right: # 합이 k를 넘으면 left를 당겨서 줄이기
            sum -= sequence[left]
            left += 1

        if sum == k:
            length = right - left
            if length < best_len:
                best_len = length
                best = [left, right]


    return best

sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence,k))