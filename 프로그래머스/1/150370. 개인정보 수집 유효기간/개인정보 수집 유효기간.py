def solution(today, terms, privacies):
    answer = []

    def to_days(date):
        y, m, d = map(int,date.split("."))
        return y*12*28 + m*28 + d

    todays = to_days(today) # 오늘 날짜 일수로 바꾸기

    term_dict = {}
    for t in terms:
        kind, months = t.split()
        term_dict[kind] = int(months)

    for idx, p in enumerate(privacies):
        date, kind = p.split()
        collectdays = to_days(date)
        # 만료일
        expiredays = collectdays + term_dict[kind] * 28 - 1

        if expiredays < todays:
            answer.append(idx+1)

    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))