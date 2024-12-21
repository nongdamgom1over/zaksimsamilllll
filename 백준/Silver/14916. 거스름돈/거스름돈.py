money = int(input())  # 거스름돈 액수 입력
res = 0  # 사용된 동전 수

while money >= 0:
    if money % 5 == 0:  # 남은 금액이 5로 나누어떨어지는 경우
        res += money // 5
        print(res)
        break
    money -= 2  # 5로 나누어떨어지지 않으면 2원짜리 동전 하나 사용
    res += 1
else:
    print(-1)  # 거슬러 줄 수 없는 경우
