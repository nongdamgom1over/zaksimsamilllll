from collections import Counter
def solution(want, number, discount):
    answer = 0
    target = {w:c for w,c in zip(want,number)}

    for start in range(len(discount)-9):
        if discount[start] in target.keys():
            if target == Counter(discount[start:start+10]):
                answer+=1

    return answer


# 테스트
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))  # 3
