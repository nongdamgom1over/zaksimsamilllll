import sys

lope = 1
arr = []
max_length = 0
result = ""
while lope<6:
    stnc = sys.stdin.readline().rstrip()
    arr.append(stnc)
    if (len(stnc)>max_length):
        max_length = len(stnc)
    lope+=1

for j in range(max_length):
    for h in range(0, 5):
        if j < len(arr[h]):
            result += arr[h][j]

print(result)