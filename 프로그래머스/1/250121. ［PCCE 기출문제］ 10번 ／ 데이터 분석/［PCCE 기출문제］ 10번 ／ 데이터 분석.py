def solution(data, ext, val_ext, sort_by):
    answer = []
    n = len(data)
    idx = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    } # DATA를 구성하는 속성들
    ext_idx = idx[ext]
    for row in data:
        if row[ext_idx] < val_ext:
            answer.append(row)

    sort_idx = idx[sort_by]
    answer.sort(key=lambda row: row[sort_idx])


    return answer