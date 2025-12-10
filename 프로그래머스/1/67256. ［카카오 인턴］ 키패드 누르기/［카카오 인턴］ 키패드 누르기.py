def solution(numbers, hand):
    pad = {
        1 : (0, 3), 2: (1, 3), 3: (2,3), 4: (0,2), 5: (1,2), 6: (2,2),
        7: (0,1), 8: (1,1), 9: (2,1), 0:(1,0)
    }
    answer = ''
    prevL = (0,0)
    prevR = (2,0)
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            prevL = pad[num]

        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            prevR = pad[num]

        else: # 중간에 있는 아이들
            l, r = 0, 0
            target = pad[num] # target까지의 길이가 몇인지
            l = abs(target[0] - prevL[0]) + abs(target[1] - prevL[1])
            r = abs(target[0] - prevR[0]) + abs(target[1] - prevR[1])
            if l<r:
                answer += "L"
                prevL = pad[num]
            elif r<l:
                answer += "R"
                prevR = pad[num]
            else:
                if hand == "right":
                    answer += "R"
                    prevR = pad[num]
                elif hand == "left":
                    answer += "L"
                    prevL = pad[num]

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))