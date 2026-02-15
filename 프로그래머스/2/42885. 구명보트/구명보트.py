from collections import deque

def solution(people, limit):
    answer = 0
    sort_people = deque(sorted(people, reverse=True))

    while sort_people:
        if len(sort_people) >= 2 and sort_people[0] + sort_people[-1] <= limit:
            sort_people.popleft()  # 무거운 사람
            sort_people.pop()      # 가벼운 사람
        else:
            sort_people.popleft()  # 무거운 사람만 혼자 탐
        answer += 1

    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))  # 3
