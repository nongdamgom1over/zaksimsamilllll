def solution(X, Y):
    countX = [0] * 10
    countY = [0] * 10

    # 각 숫자 개수 세기
    for ch in X:
        countX[int(ch)] += 1
    for ch in Y:
        countY[int(ch)] += 1

    result = []

    # 9부터 0까지 공통 개수만큼 추가
    for num in range(9, -1, -1):
        common = min(countX[num], countY[num])
        result.append(str(num) * common)

    result = "".join(result)

    # 공통 숫자가 없으면 -1
    if result == "":
        return "-1"

    # 0만 잔뜩 있는 경우
    if result[0] == "0":
        return "0"

    return result
