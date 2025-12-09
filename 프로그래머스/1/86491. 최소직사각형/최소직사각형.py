def solution(sizes):
    max_w = -1
    max_h = -1
    for w,h in sizes:
        long_side = max(w,h)
        short_side = min(w,h)

        max_w = max(max_w, long_side)
        max_h = max(max_h, short_side)

    return max_w * max_h