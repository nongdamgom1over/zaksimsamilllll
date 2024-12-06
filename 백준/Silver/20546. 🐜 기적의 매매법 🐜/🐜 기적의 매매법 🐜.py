def junhyun(money, juga):
    stocks = 0  # 보유 주식 수

    for price in juga:
        if money >= price:  # 매수 가능한 경우
            stocks += money // price
            money %= price  # 잔액 계산

    # 최종 자산 = 남은 현금 + (보유 주식 수 × 마지막 날 주가)
    return money + stocks * juga[-1]


def sungmin(money, juga):
    stocks = 0  # 보유 주식 수
    up_count = 0  # 연속 상승 일수
    down_count = 0  # 연속 하락 일수

    for i in range(1, len(juga)):
        if juga[i] > juga[i - 1]:  # 전날보다 상승
            up_count += 1
            down_count = 0
        elif juga[i] < juga[i - 1]:  # 전날보다 하락
            down_count += 1
            up_count = 0
        else:  # 가격 동일
            up_count = 0
            down_count = 0

        # 3일 연속 상승 -> 전량 매도
        if up_count >= 3 and stocks > 0:
            money += stocks * juga[i]
            stocks = 0

        # 3일 연속 하락 -> 전량 매수
        if down_count >= 3 and money >= juga[i]:
            stocks += money // juga[i]
            money %= juga[i]

    # 최종 자산 = 남은 현금 + (보유 주식 수 × 마지막 날 주가)
    return money + stocks * juga[-1]


# 입력 처리
money = int(input().strip())  # 초기 현금
juga = list(map(int, input().split()))  # 14일간의 주가

# 자산 계산
junhyun_asset = junhyun(money, juga)
sungmin_asset = sungmin(money, juga)

# 결과 출력
if junhyun_asset > sungmin_asset:
    print("BNP")
elif junhyun_asset < sungmin_asset:
    print("TIMING")
else:
    print("SAMESAME")
