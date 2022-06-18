hw = list(map(int, input().split()))
h = hw[:3]
w = hw[3:]
ans = 0
for i in range(1, 30):
    for j in range(1, 30):
        for k in range(1, 30):
            for l in range(1, 30):
                if not 0 < h[0] - i - j < 30:
                    continue
                if not 0 < h[1] - k - l < 30:
                    continue
                if not 0 < w[0] - i - k < 30:
                    continue
                if not 0 < w[1] - j - l < 30:
                    continue
                if not (0 < w[2] - (h[0] - i - j) - (h[1] - k - l) < 30):
                    continue
                if (w[2] - (h[0] - i - j) - (h[1] - k - l)) != (h[2] - (w[0] - i - k) - (w[1] - j - l)):
                    continue
                ans += 1
print(ans)
