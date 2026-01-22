def solution(picks, minerals):
    answer = 0 # 피로도
    max_mine = sum(picks)*5
    r = min(max_mine, len(minerals))
    chunks = []
    for start in range(0,max_mine,5):
        d,i,s = 0,0,0
        for k in range(start,min(start+5, r)):
            if minerals[k] == "diamond":
                d+=1
            elif minerals[k] == "iron":
                i+=1
            elif minerals[k] == "stone":
                s+=1
            else:
                break
        chunks.append((d,i,s))

    # 정렬
    chunks.sort(key=lambda x:x[0]*25+x[1]*5+x[2], reverse=True)

    # 곡괭이 배정
    for d,i,s in chunks:
        if picks[0]>0:
            answer+=d+i+s
            picks[0]-=1
        elif picks[1]>0:
            answer+=d*5+i+s
            picks[1]-=1
        elif picks[2]>0:
            answer+=d*25+i*5+s
            picks[2]-=1
        else:
            break

    return answer

picks = [0, 1, 1] # 다곡/철곡/돌곡
minerals = ["diamond", "diamond", "diamond",
            "diamond", "diamond", "iron", "iron", "iron",
            "iron", "iron", "diamond"]
print(solution(picks,minerals))