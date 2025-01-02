import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().rstrip().split())

# 분모 확인
denominator = a * e - b * d
if denominator == 0:
    print("Invalid input: denominator is zero")
    sys.exit(1)  # 강제 종료

# x 계산
x = (c * e - b * f) // denominator

# y 계산 (b == 0인 경우 처리)
if b != 0:
    y = (c - a * x) // b
else:
    y = (f - d * x) // e

print(f"{x} {y}")
