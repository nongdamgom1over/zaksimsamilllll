import heapq

def solution(book_time):
    times = []

    def to_min(time):
        h, m = time.split(":")
        return int(h) * 60 + int(m)

    for s, e in book_time:
        start = to_min(s)
        end = to_min(e) + 10
        times.append((start, end))

    times.sort()

    heap = []
    answer = 0

    for s, e in times:
        if heap and heap[0] <= s:   # s: 현재 예약 시작시간
            heapq.heappop(heap)
        heapq.heappush(heap, e)
        answer = max(answer, len(heap))

    return answer


book_time = [["09:10", "10:10"], ["10:20", "12:20"]]
print(solution(book_time))