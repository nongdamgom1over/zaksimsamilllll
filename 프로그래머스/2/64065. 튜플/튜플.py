def solution(s):
    answer = []
    # 집합 문자열을 숫자 리스트로 변환
    s = s.strip("{}")
    parts = s.split("},{")
    sets = [list(map(int, p.replace("{","").replace("}","").split(","))) for p in parts]
    sets.sort(key=len)
    for group in sets:
        for num in group:
            if num not in answer:
                answer.append(num)

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))