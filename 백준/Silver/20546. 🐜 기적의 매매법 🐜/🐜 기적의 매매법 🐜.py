import sys

def junhyun(money, juga):
    amount = 0 # 준현이 최종 주가
    x = 0
    for i in range(14):
        if (juga[i] <= money): # 보유 현금이 주가보다 높은 경우 매수
            x += money // juga[i] # 구매 주 수
            money = money % juga[i] # 구매 잔액
        else:
            continue
    amount = juga[13]*x + money
    return amount

def sungmin(money, juga):
    amount = 0
    x = 0 # 구매 주 수
    state = [] # 업(T)인지 다운(F)인지 F/T로 구별
    for i in range(14):
        if (i > 0): # i가 0이상인 경우만
            if (juga[i-1] < juga[i]): #전일보다 주가가 오름
                state.append(True)
            else: #같거나 작음
                state.append(False)

            if (i > 3):
                if (state[i-3] == True and state[i-2]==True and state[i-1] == True): #연속 오름
                    money += juga[i]*x
                    x = 0
                elif (state[i-3] == False and state[i-2]==False and state[i-1] == False): # 연속 내림
                    x += money // juga[i]
                    money = money % juga[i]  # 구매 잔액

    amount = juga[13]*x + money
    return amount

# 입력
money = int(sys.stdin.readline().rstrip()) # 둘에게 주어진 현금
juga = map(int, input().split(" ")) # 14일 간의 주가
juga = list(juga)

a = junhyun(money, juga)
b = sungmin(money, juga)

if a>b :
    print("BNP")
elif b>a:
    print("TIMING")
else:
    print("SAMESAME")
