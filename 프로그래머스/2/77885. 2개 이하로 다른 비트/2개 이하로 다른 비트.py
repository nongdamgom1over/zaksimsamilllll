import math
def solution(numbers):
    answer = []
    # f(x) : x보다 크고 x와 비트가 1~2개 다른 수 중 제일 작은 수
    ## f(2) > 0000 0010 >> 0000 0011 = 3
    ## f(7) > 0000 0111 >> 0000 1011 = 11

    for i in range(len(numbers)):
        bin_num = str(bin(numbers[i])[2:])
        if numbers[i] % 2 == 0:
            answer.append(numbers[i]+1)
        else:
            b = '0' + bin(numbers[i])[2:]  # 앞에 0 하나 붙이기
            idx = b.rfind('0')  # 가장 오른쪽 0 찾기

            # 그 0을 1로 바꾸고, 바로 다음 비트를 0으로
            b = b[:idx] + '10' + b[idx + 2:]

            answer.append(int(b, 2))

    return answer

numbers = [2,7]
print(solution(numbers))