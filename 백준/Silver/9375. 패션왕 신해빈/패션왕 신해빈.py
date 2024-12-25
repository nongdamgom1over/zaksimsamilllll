import sys
from collections import defaultdict

# 테스트 케이스 수 입력
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    clothes = defaultdict(int)  # 의상의 종류별 개수를 저장

    for _ in range(n):
        _, kind = sys.stdin.readline().rstrip().split()  # 이름은 필요 없고 종류만 사용
        clothes[kind] += 1

    # 모든 종류의 의상에서 한 가지씩 선택하는 경우의 수 계산
    result = 1
    for count in clothes.values():
        result *= (count + 1)  # 해당 종류를 입지 않는 경우 포함

    # 아무것도 입지 않은 경우를 제외
    print(result - 1)
