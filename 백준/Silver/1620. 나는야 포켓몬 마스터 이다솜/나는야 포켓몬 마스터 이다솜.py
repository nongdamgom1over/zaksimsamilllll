import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" ")) # n 포켓몬의 개수, m 맞춰야하는 문제의 개수
poke = {}
for i in range(1,n+1):
    name = sys.stdin.readline().rstrip()
    poke[i] = name
    poke[name] = i

for _ in range(m):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(poke[int(question)])
    else:
        print(poke[question])