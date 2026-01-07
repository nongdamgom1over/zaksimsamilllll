from collections import Counter

def solution(topping):
    right = Counter(topping)   # 오른쪽에 전체가 있다고 시작
    left_set = set()
    right_kinds = len(right)
    answer = 0

    # i에서 자른다는 건: topping[i]는 왼쪽에 포함, i+1부터 오른쪽
    # 그래서 끝 원소는 왼쪽으로 옮기고 자를 수 없으니 n-1까지만
    for i in range(len(topping) - 1):
        x = topping[i]

        # 왼쪽에 추가
        left_set.add(x)

        # 오른쪽에서 제거(1개 이동)
        right[x] -= 1
        if right[x] == 0:
            del right[x]
            right_kinds -= 1

        if len(left_set) == right_kinds:
            answer += 1

    return answer
