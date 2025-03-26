def solution(n, m):
    res = 1
    for i in range(n):
        res = res * (i + 1)
    for j in range(m):
        res = res // (j + 1)  # 나눗셈을 //로 변경 (정수 유지)
    for l in range(n - m):
        res = res // (l + 1)
    return res

if __name__ == '__main__':
    n, m = map(int, input().split())
    res = solution(n, m)
    print(res)
