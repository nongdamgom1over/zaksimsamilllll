def solution(picks, minerals):
    answer = 0 # 피로도

    max_mine = sum(picks) * 5 # 캘 수 잇는 최대 광물
    minerals = minerals[:max_mine]
    chunks = []
    for start in range(0, len(minerals), 5):
        d, i, s = 0, 0, 0
        for k in range(start, min(start + 5, len(minerals))):
            if minerals[k] == "diamond":
                d += 1
            elif minerals[k] == "iron":
                i+=1
            elif minerals[k] == "stone":
                s+=1
        chunks.append((d,i,s))
    # stone 기준 피로도 계산 > 내림차순
    chunks.sort(key=lambda x: x[0]*25 + x[1]*5 + x[2], reverse=True)

    # 곡괭이 배치
    for d,i,s in chunks:
        if picks[0] > 0: # 다곡
            answer+=d+i+s
            picks[0]-=1
        elif picks[1] > 0: # 철곡
            answer+=d*5+i+s
            picks[1]-=1
        elif picks[2] > 0: # 돌곡
            answer+= d*25 + i*5 + s
            picks[2]-=1
        else: # 곡괭이 선택 불가
            break

    return answer

picks = [0, 1, 1] # 다곡/철곡/돌곡
minerals = ["diamond", "diamond", "diamond",
            "diamond", "diamond", "iron", "iron", "iron",
            "iron", "iron", "diamond"]
print(solution(picks,minerals))