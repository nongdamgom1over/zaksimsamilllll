import sys

def min_swaps_to_make_a_continuous(s):
    n = len(s)
    a_count = s.count('a')  # 총 'a'의 개수
    if a_count == 0 or a_count == n:  # 'a'가 없거나 전체가 'a'인 경우
        return 0

    # 문자열을 2배로 확장하여 원형 처리를 모방
    s = s + s

    # 초기 윈도우에서 'b'의 개수 계산
    b_count = s[:a_count].count('b') #문자열의 처음~a의 갯수까지 잘라서 b의 갯수 세기
    min_swaps = b_count

    # 슬라이딩 윈도우
    for i in range(1, n):
        # 윈도우의 오른쪽 문자 추가, 왼쪽 문자 제거
        if s[i - 1] == 'b':  # 이전 윈도우의 시작 문자 제거
            b_count -= 1
        if s[i + a_count - 1] == 'b':  # 현재 윈도우의 끝 문자 추가
            b_count += 1

        # 최소 교환 횟수 갱신
        min_swaps = min(min_swaps, b_count)

    return min_swaps

# 입력
s = sys.stdin.readline().rstrip()
print(min_swaps_to_make_a_continuous(s))
