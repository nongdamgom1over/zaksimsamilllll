import sys

# 입력
N, B = input().split(" ")
B = int(B)
N = ''.join(reversed(N)) #진법은 끝에서 부터 보니까
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = 0

for x,w in enumerate(N):
    res += (B**x) * (num_list.index(w))
print(res)