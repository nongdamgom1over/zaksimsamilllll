def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    # 뒷큰수를 못찾은 인덱스들은 저장
    stack = [] # 인덱스 값을 저장
    for i in range(n):
        while stack and numbers[i] > numbers[stack[-1]]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i)
    return answer
