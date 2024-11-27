string = input().upper()
new_string = list(set(string))  ##중복 제거

n = []  ##문자열 반복 수 저장할 거임

for i in new_string:
    n.append(string.count(i))

if n.count(max(n)) >= 2:
    print("?")

else:
    print(new_string[(n.index(max(n)))])