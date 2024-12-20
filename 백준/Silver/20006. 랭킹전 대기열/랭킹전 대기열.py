import sys

# 입력 받기
p, m = map(int, sys.stdin.readline().split())
players = []

# 플레이어 정보 입력 받기
for _ in range(p):
    l, n = sys.stdin.readline().split()
    l = int(l)
    players.append((l, n))

# 매칭 시스템
rooms = []

for level, nickname in players:
    matched = False
    for room in rooms:
        # 방에 입장할 수 있는 조건 확인
        if len(room) < m and (room[0][0] - 10 <= level <= room[0][0] + 10):
            room.append((level, nickname))
            matched = True
            break
    # 매칭 가능한 방이 없다면 새 방 생성
    if not matched:
        rooms.append([(level, nickname)])

# 출력
for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    # 닉네임을 사전순으로 정렬하여 출력
    for l, n in sorted(room, key=lambda x: x[1]):
        print(l, n)
