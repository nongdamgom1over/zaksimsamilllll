def solution(cards1, cards2, goal):
    n, m = len(cards1), len(cards2)
    i, j = 0, 0

    for word in goal:
        if i<n and cards1[i] == word:
            i+=1
        elif j<m and cards2[j] == word:
            j+=1
        else:
            return "No"

    return "Yes"