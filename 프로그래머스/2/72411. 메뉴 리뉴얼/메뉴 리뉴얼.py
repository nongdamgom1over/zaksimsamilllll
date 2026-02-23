from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    # 1️⃣ 모든 주문을 알파벳 순으로 정렬
    orders = ["".join(sorted(order)) for order in orders]

    # 2️⃣ 코스 길이 하나씩 순회
    for k in course:
        # 3️⃣ 길이 k인 조합들을 카운트할 Counter 생성
        comb_counter = Counter()

        # 4️⃣ 각 주문에 대해
        #    - 주문 길이가 k 이상이면
        #    - combinations(order, k) 생성
        #    - comb_counter에 +1씩 카운트
        for order in orders:
            for comb in combinations(order, k):
                comb_counter[comb] += 1

        # 5️⃣ k 길이에서 가장 많이 등장한 횟수 찾기
        # max_count = ?
        # 단, 최소 2번 이상 등장한 조합만 고려
        max_count = max(comb_counter.values())
        if max_count >= 2:
            for key, value in comb_counter.items():
                if value == max_count:
                    answer.append("".join(key))


        # 6️⃣ max_count와 같은 조합들을 answer에 추가
        # 조합(tuple)을 문자열로 변환해서 추가
        answer.sort()

    # 7️⃣ 최종 answer를 사전순 정렬
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))
