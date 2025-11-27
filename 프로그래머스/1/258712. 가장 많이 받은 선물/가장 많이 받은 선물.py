def solution(friends, gifts):
    answer = 0
    n = len(friends)
    # 1. friends 리스트의 각 이름을 숫자(index)로 매핑하는 딕셔너리 생성
    idx = {f: i for i, f in enumerate(friends)}
    # 딕셔너리컴프리헨션 { key_expression : value_expression  for 반복문 }

    # 2: A→B 선물 횟수를 저장하는 2차원 배열 만들기
    gift_cnt = [[0] * n for _ in range(n)]
    for g in gifts:
        a,b = g.split(" ")
        gift_cnt[idx[a]][idx[b]] += 1

    # 3: 각 사람의 선물 지수
    give = [0] * n
    receive = [0] * n
    for i in range(n):
        for j in range(n):
            give[i] += gift_cnt[i][j]
            receive[j] += gift_cnt[i][j]

    gift_score = [give[i] - receive[i] for i in range(n)]

    # 4: 선물계산
    next_month = [0]*n

    for i in range(n):
        for j in range(i+1,n): #쌍 한번씩만 판별
            a_to_b = gift_cnt[i][j]
            b_to_a = gift_cnt[j][i]

            if a_to_b > b_to_a:
                next_month[i] += 1
            elif b_to_a > a_to_b:
                next_month[j] += 1
            else: # 같으면 선물지수로
                if gift_score[i] > gift_score[j]:
                    next_month[i] += 1
                elif gift_score[j] > gift_score[i]:
                    next_month[j] += 1

    # 5단계: 다음달 받을 선물 카운트에서 가장 큰 값 출력
    answer = max(next_month)
    return answer