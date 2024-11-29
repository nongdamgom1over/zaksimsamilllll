import sys

N, M = map(int, input().split(" "))
words = dict()


for i in range(N): # 입력 받기
    word = sys.stdin.readline().rstrip()
    if (len(word)>= M): # 최소 단어 길이 만족하는가
        if (word in words):
            words[word] += 1

        else:
            words[word] = 1

# 규칙에 따라 정렬 (rule1 -> rule2 -> rule3)
sorted_words = sorted(
    words.items(),
    key=lambda x: (-x[1], -len(x[0]), x[0])  # 등장 횟수, 길이, 사전 순
)


# 결과 출력
for word, _ in sorted_words:
    print(word)