import sys

T = int((input()))

for i in range(0,T):
    dic = dict()
    stnc = sys.stdin.readline().rstrip()
    stnc = stnc.replace(" ","")
    for j in range(0, len(stnc)):
        if stnc[j] in dic:
            dic[stnc[j]] += 1
        else:
            dic[stnc[j]] = 1
    tmp = [k for k, v in dic.items() if max(dic.values()) == v]
    if (len(tmp)>1) :
         print("?")
    else:
        max_key = max(dic, key=dic.get)
        print(max_key)

