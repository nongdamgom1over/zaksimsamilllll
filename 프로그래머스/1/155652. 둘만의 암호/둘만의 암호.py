def solution(s, skip, index):
    answer = ''
    skip_set = set(skip)

    for word in s:
        cnt = 0
        cur = ord(word)
        while cnt<index:
            cur+=1
            if cur > ord('z'):
                cur = ord('a')
            if chr(cur) in skip_set:
                continue
            cnt+=1

        answer+=chr(cur)

    return answer