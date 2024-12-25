import sys
from math import gcd
from itertools import combinations  # 조합 사용

t = int(sys.stdin.readline().rstrip())  # 테스트 케이스의 개수

for _ in range(t):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    n = data[0]  # 수의 개수
    numbers = data[1:]  # 실제 수들

    # 모든 가능한 쌍의 GCD의 합 계산
    total_gcd_sum = 0
    for a, b in combinations(numbers, 2):  # combinations으로 쌍 생성
        total_gcd_sum += gcd(a, b)

    print(total_gcd_sum)
