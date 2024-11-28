import sys

listen, see = map(int, input().split(" "))

a = set() # 집합 자료형 - 중복x, 정렬x (sorted를 함해야됨)
b = set()

for i in range(listen):
    a.add(sys.stdin.readline().rstrip())

for i in range(see):
    b.add(sys.stdin.readline().rstrip())

res = sorted(a & b) #새로운 정렬 리스트 만들기

print(len(res))
for i in res:
    print(i)

















