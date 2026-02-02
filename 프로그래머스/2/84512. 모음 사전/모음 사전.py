def solution(word):
    answer = 0
    dictionary = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    # 가중치 구하기
    weight = [0] * 5
    weight[-1] = 1
    for i in range(3,-1,-1):
        weight[i] = weight[i+1]*5 + 1
    
    for idx, ch in enumerate(word):
        answer += weight[idx] * dictionary[ch] + 1
    
    return answer

