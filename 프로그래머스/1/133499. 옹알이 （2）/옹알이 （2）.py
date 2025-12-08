def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        idx = 0
        prev = '' #직전에 사용한 발음
        ok = True

        while idx<len(b):
            matched = False
            for word in words:
                if word == prev:
                    continue
                if b.startswith(word,idx):
                    matched = True
                    prev = word
                    idx += len(word)
                    break

            if not matched:
                ok = False
                break
        if ok and idx == len(b):
            answer+=1

    return answer