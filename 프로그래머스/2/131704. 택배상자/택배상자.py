def solution(order):
    answer = 0
    n = len(order)
    stack = []
    last = 1
    i = 0 # order 인덱스
    while True:
        # 보조 벨트에 원하는 거 있으면 실어버리기
        if stack and stack[-1] == order[i]:
            stack.pop()
            answer+=1
            i += 1
            if i == n:
                break
            continue

        # 메인 벨트에 원하는거 있는지
        if last<=n: # 메인에서 더 꺼낼 수 있는가
            if order[i] == last:
                answer+=1
                last+=1
                i+=1
                if n==i:
                    break
            else:
                stack.append(last)
                last+=1
            continue

        break

    return answer

order = [4, 3, 1, 2, 5]
print(solution(order))