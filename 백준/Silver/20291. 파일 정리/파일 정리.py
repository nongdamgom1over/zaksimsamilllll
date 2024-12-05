import sys

# 입력 받기
N = int(sys.stdin.readline().rstrip())  # 문자열 입력
file = dict()

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    exten = []
    exten = word.split(".")
    if exten[-1] in file:
        file[exten[-1]] += 1
    else:
        file[exten[-1]] = 1

file = sorted(file.items(), key=lambda x:x[0])

for key, value in file:
    print(f"{key} {value}")