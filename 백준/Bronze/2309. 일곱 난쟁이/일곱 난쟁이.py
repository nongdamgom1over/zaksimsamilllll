import sys
from itertools import combinations

# 아홉 난쟁이들의 키 입력
height = []

for _ in range(9):
    temp = int(sys.stdin.readline().rstrip())
    height.append(temp)

# 7명의 난쟁이 조합 생성
dwarf_combinations = combinations(height, 7)

# 합이 100인 조합 찾기
for dwarf in dwarf_combinations:
    if sum(dwarf) == 100:
        result = sorted(dwarf)  # 결과를 오름차순으로 정렬
        for h in result:
            print(h)
        break  # 하나의 정답만 찾으면 종료
