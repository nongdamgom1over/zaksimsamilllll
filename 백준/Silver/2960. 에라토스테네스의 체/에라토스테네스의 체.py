import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

cnt = 0  # K번째 지워진 수를 추적하기 위한 변수
li = [False] * (n + 1)  # 숫자가 지워졌는지 표시하기 위한 배열 (0부터 시작)

for p in range(2, n + 1):
    if not li[p]:  # 아직 지워지지 않은 수라면
        for multiple in range(p, n + 1, p):  # P의 배수를 모두 순회
            if not li[multiple]:  # 아직 지워지지 않은 배수라면
                li[multiple] = True  # 지움 처리
                cnt += 1  # 지워진 수 카운트 증가
                if cnt == k:  # K번째 지운 수를 찾은 경우
                    print(multiple)  # 결과 출력
                    exit()  # 프로그램 종료
