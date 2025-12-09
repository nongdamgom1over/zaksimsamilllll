def solution(n):
    answer = ""
    arr = []
    while n > 0:
        arr.append(n % 10)
        n=n//10

    arr.sort(reverse=True)
    for value in arr:
        answer+=str(value)

    return int(answer)