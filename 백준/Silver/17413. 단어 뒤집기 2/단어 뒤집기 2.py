import sys

# 입력 받기
input_str = sys.stdin.readline().rstrip()  # 문자열 입력
state = False  # False: 단어 입력 모드, True: 태그 입력 모드
re_str = []  # 최종 결과를 저장할 리스트
word = []  # 단어를 임시로 저장
tag = []  # 태그를 임시로 저장

for char in input_str:
    if not state:  # 단어 입력 모드
        if char == '<':  # 태그 시작
            if word:  # 현재까지 저장된 단어를 뒤집어서 추가
                re_str.append(''.join(reversed(word)))
                word.clear()
            state = True
            tag.append(char)
        elif char == ' ':  # 단어 끝 (공백)
            if word:
                re_str.append(''.join(reversed(word)))
                word.clear()
            re_str.append(char)  # 공백 추가
        else:  # 일반 문자
            word.append(char)
    else:  # 태그 입력 모드
        if char == '>':  # 태그 끝
            tag.append(char)
            re_str.append(''.join(tag))  # 태그를 그대로 추가
            tag.clear()
            state = False
        else:
            tag.append(char)

# 남아 있는 단어 처리
if word:
    re_str.append(''.join(reversed(word)))

# 결과 출력
print(''.join(re_str))
