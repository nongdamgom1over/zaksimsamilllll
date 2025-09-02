if __name__ == '__main__':
    H, W, N, M = map(int, input().split())

    # 거리두기를 고려한 좌석 간격은 (N+1), (M+1)
    rows = (H + N) // (N + 1)
    cols = (W + M) // (M + 1)

    print(rows * cols)
