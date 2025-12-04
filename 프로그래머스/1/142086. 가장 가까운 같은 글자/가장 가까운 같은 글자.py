def solution(s):
    answer = []

    dictionary = {}
    idx = 0
    for ch in s:
        if ch not in dictionary:
            dictionary[ch] = idx
            answer.append(-1)
        else:
            answer.append(idx - dictionary[ch])
            dictionary[ch] = idx
        idx += 1

    return answer