from math import gcd, isqrt
def solution(arrayA, arrayB):
    def gcd_of_list(arr):
        g = 0
        for x in arr:
            g = gcd(g, x)
        return g

    def get_divisors_desc(n):
        small, large = [], []
        r = isqrt(n)
        for i in range(1, r + 1):
            if n % i == 0:
                small.append(i)
                if i * i != n:
                    large.append(n // i)
        # 큰 것부터: large는 이미 큰 쪽(대략 내림), small은 오름 -> 뒤집어서 큰 쪽
        return sorted(large, reverse=True) + sorted(small, reverse=True)

    def valid(a, other_arr):
        # other_arr의 어떤 원소도 a로 나누어 떨어지면 안 됨
        for x in other_arr:
            if x % a == 0:
                return False
        return True

    def best_candidate(g, other_arr):
        # g의 약수 중 조건 만족하는 최대값 찾기
        for d in get_divisors_desc(g):
            if d > 1 and valid(d, other_arr):
                return d
        return 0
    gA = gcd_of_list(arrayA)
    gB = gcd_of_list(arrayB)

    candA = best_candidate(gA, arrayB)  # A는 다 나누고, B는 하나도 못 나누는 최대
    candB = best_candidate(gB, arrayA)  # 반대

    return max(candA, candB)


arrayA = [14, 35, 119]
arrayB = [18, 30, 102]

print(solution(arrayA,arrayB))