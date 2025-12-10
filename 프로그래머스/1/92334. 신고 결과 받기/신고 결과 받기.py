def solution(id_list, report, k):
    report_board = {id:0 for id in id_list}
    answer = [0] * len(id_list)
    unique_report = set(report) # 유니크한 리포트만 남기기 위해 set 문자열 사용

    for i in unique_report:
        user, reported_user = i.split(" ")
        report_board[reported_user] += 1

    for r in unique_report:
        user, reported_user = r.split(" ")
        if report_board[reported_user] >= k:
            answer[id_list.index(user)] += 1
    
    return answer