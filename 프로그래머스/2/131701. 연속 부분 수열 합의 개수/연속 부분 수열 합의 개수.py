def solution(elements):
    l = len(elements)
    circle = elements * 2
    sums = set()

    for i in range(1,l+1):
        for start in range(l):
            sums.add(sum(circle[start:start + i]))
    return len(sums)

elements = [7,9,1,1,4]
print(solution(elements))