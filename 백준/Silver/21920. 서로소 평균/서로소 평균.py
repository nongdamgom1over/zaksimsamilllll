import sys

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n = int(sys.stdin.readline().rstrip())  # 입력될 수들의 개수
a = list(map(int, sys.stdin.readline().rstrip().split(" ")))  # 수열
x = int(sys.stdin.readline().rstrip())  # a와 서로소인 숫자를 찾을 수
cnt = 0
total = 0  # sum 대신 다른 이름을 사용 (sum은 내장 함수 이름과 겹칠 수 있음)

for i in range(n):
    smaller = min(a[i], x)  # a를 덮어쓰지 않고 새로운 변수 사용
    larger = max(a[i], x)
    if gcd(smaller, larger) == 1:  # 서로소
        cnt += 1
        total += a[i]  # 누적합 계산
    else:
        continue

# 나누기 전에 cnt가 0인지 확인 (ZeroDivisionError 방지)
if cnt > 0:
    print(f"{total / cnt:.6f}")
else:
    print(0)  # 서로소가 없으면 0 출력