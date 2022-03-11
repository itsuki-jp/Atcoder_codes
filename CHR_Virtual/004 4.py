N = int(input())
for h in range(1, 3501):
    for n in range(1, 3501):
        if (4 * h * n - n * N - h * N) > 0 and (h * n * N) % (4 * h * n - n * N - h * N) == 0:
            w = (h * n * N) // (4 * h * n - n * N - h * N)
            if w >= 0:
                print(h, n, w)
                exit()
