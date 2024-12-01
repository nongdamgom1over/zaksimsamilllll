import sys

str = sys.stdin.readline().rstrip()

# 알파벳 등장 횟수를 저장하는 딕셔너리
dic = {}
for char in str:
    dic[char] = dic.get(char, 0) + 1

# 홀수 개수 알파벳 확인
odd = [char for char in dic if dic[char] % 2 != 0]

# 홀수 개수 알파벳이 2개 이상이면 팰린드롬 불가능
if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    # 팰린드롬 앞부분 구성
    re_str = []
    for char in sorted(dic):  # 사전 순 정렬
        count = dic[char] // 2
        re_str.extend(char * count)

    front = ''.join(re_str)
    middle = odd[0] if odd else ''  # 홀수 알파벳이 있으면 중앙에 추가
    end = ''.join(reversed(re_str))

    print(front + middle + end)
