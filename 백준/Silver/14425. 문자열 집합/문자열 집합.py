import sys

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
s = set(data[1:n+1])
cnt = sum(1 for str in data[n+1:n+1+m] if str in s)

print(cnt)
