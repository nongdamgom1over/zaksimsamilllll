def solution(k, tangerine):
    answer = 0
    count = {}
    for t in tangerine:
        if t not in count:
            count[t] = 1
        else:
            count[t] += 1

    count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    # 이중에서 k개를 뽑아야되고 x[1] 값을 더해서 k개가 되게
    n = 0
    for idx, v in count:
        if n >= k:
            break
        n+=v
        answer+=1

    return answer
