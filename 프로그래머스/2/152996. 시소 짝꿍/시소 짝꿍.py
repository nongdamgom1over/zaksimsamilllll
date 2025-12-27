def solution(weights):
    answer = 0
    w_count = {}
    for w in weights:
        if w in w_count:
            w_count[w] += 1
        else:
            w_count[w] = 1
    # 같은 몸무게 까지
    for w,c in w_count.items():
        if c>=2:
            answer += c * (c-1) // 2
    ratios = [(2,3), (2,4), (3,4)]
    for w,c in w_count.items():
        for a,b in ratios:
            target = w*a/b
            if target.is_integer() and target in w_count:
                answer+= c * w_count[int(target)]


    return answer

weights = [100,180,360,100,270]
print(solution(weights))