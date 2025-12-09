def solution(price, money, count):
    hap = [x for x in range(1,count+1)]
    ret = (sum(hap) * price) - money
    if ret < 0:
        return 0
    return ret