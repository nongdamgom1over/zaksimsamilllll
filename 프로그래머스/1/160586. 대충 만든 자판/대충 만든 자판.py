def solution(keymap, targets):
    # 1. 각 문자별 최소 누름 횟수 저장
    min_press = {}

    for key in keymap:
        for idx, char in enumerate(key):
            # idx는 0-based, 실제 누름 횟수는 idx+1
            presses = idx + 1
            if char not in min_press or presses < min_press[char]:
                min_press[char] = presses

    # 2. 각 target 계산
    answer = []
    for target in targets:
        total = 0
        possible = True
        for ch in target:
            if ch not in min_press:
                possible = False
                break
            total += min_press[ch]

        if possible:
            answer.append(total)
        else:
            answer.append(-1)

    return answer
