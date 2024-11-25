import sys

num = 0
dic = dict()

while 1:
    species = sys.stdin.readline().rstrip()
    if species == '':
        break
    num += 1
    if species in dic:
        dic[species] += 1
    else:
        dic[species] = 1

sorted_dic=dict(sorted(dic.items()))

for i in sorted_dic:
    val = sorted_dic[i]
    per = (val / num * 100)

    print("%s %.4f" %(i, per))
