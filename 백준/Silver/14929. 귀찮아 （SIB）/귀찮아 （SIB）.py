def calculate_sum(n, x):
    total_sum = sum(x)  # 전체 합
    square_sum = sum(num ** 2 for num in x)  # 각 원소의 제곱합

    # 결과 계산
    result = (total_sum ** 2 - square_sum) // 2
    return result


# 입력
n = int(input())
x = list(map(int, input().split()))

# 출력
print(calculate_sum(n, x))
