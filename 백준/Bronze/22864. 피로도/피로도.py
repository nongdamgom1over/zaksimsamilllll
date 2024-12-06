# 입력
A, B, C, M = map(int, input().split())

# 초기값
heart = 0  # 현재 피로도
work = 0   # 하루 일 처리량

# 24시간 반복
for _ in range(24):
    if heart + A <= M:  # 일을 해도 피로도가 최대치를 넘지 않을 경우
        work += B       # 처리한 일 추가
        heart += A      # 피로도 증가
    else:               # 일을 하면 피로도가 넘는 경우 -> 휴식
        heart -= C      # 피로도 감소
        if heart < 0:   # 피로도는 0 이하가 될 수 없음
            heart = 0

# 결과 출력
print(work)
