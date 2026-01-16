import heapq
def solution(n, k, enemy):
    answer = 0
    heap = []
    # 무적권을 어디다쓰면 좋을까?
    for x in enemy:
        n -= x
        heapq.heappush(heap, -x)

        if n < 0:
            if k>0:
                largest = -heapq.heappop(heap)  # heappop > 가장 작은 값 꺼냄
                n += largest
                k -= 1
                if n<0:
                    break
            else:
                break
        answer += 1
    return answer

n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]
print(solution(n,k,enemy))