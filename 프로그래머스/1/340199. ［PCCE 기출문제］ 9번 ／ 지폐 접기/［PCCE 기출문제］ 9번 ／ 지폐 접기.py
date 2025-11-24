def solution(wallet, bill):
    answer = 0
    wallet.sort() #[0]>[1]
    bill.sort() #[0]>[1]

    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        if bill[0] > bill[1]:
            bill[0] //= 2
            bill.sort()
            answer+=1
        elif bill[1] > bill[0]:
            bill[1] //= 2
            bill.sort()
            answer += 1

    return answer