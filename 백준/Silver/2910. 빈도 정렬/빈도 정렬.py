import sys

# 입력 받기
n, c = map(int, sys.stdin.readline().rstrip().split(" "))
value = list(map(int, sys.stdin.readline().rstrip().split(" ")))

# 각 숫자의 빈도 계산 및 첫 등장 순서 저장
res = {}
order = {}  # 숫자의 첫 등장 순서를 저장
for i in range(n):
    if value[i] not in res:
        res[value[i]] = 1
        order[value[i]] = i
    else:
        res[value[i]] += 1

# 빈도 정렬
s_res = sorted(value, key=lambda x: (-res[x], order[x]))

# 결과 출력
print(" ".join(map(str, s_res)))