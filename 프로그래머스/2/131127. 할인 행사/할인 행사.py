def solution(want, number, discount):
    answer = 0

    # 목표 수량
    target = {w: c for w, c in zip(want, number)}

    # 현재 10일 윈도우 카운트(원하는 품목만 관리)
    window = {w: 0 for w in want}

    m = len(discount)

    # 1) 첫 10일 채우기
    for i in range(10):
        item = discount[i]
        if item in window:
            window[item] += 1

    # 비교 함수: want 품목들의 개수가 전부 일치하는지
    def is_match():
        for w in want:
            if window[w] != target[w]:
                return False
        return True

    if is_match():
        answer += 1

    # 2) 슬라이딩 (start = 1 ~ m-10)
    for start in range(1, m - 9):
        out_item = discount[start - 1]
        in_item = discount[start + 9]

        if out_item in window:
            window[out_item] -= 1
        if in_item in window:
            window[in_item] += 1

        if is_match():
            answer += 1

    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))