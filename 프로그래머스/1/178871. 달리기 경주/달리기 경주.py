def solution(players, callings):
    pos = {player: i for i, player in enumerate(players)}

    for name in callings:
        idx = pos[name]
        front = players[idx-1]

        # 앞이랑 자리 바꾸기
        players[idx], players[idx-1] = players[idx-1], players[idx]

        #pos에 등수 반영
        pos[name] -= 1
        pos[front] += 1


    return players