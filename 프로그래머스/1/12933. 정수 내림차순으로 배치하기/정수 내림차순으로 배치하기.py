def solution(n):
    answer = ""
    arr = []
    while n > 0:
        arr.append(n % 10)
        n=n//10

    arr.sort(reverse=True)

    return int("".join(map(str,arr)))

n = 118372
print(solution(n))