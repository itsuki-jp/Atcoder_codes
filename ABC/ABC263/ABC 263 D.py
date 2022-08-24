from itertools import accumulate

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
acc = [0] + list(accumulate(A))
r_acc = [(N - r) * R + acc[r] for r in range(N + 1)]
l_acc = [l * L - acc[l] for l in range(N + 1)]
r_min = r_acc[::]
for _ in range(N - 1, -1, -1):
    r_min[_] = min(r_min[_ + 1], r_acc[_])

ans = float("inf")
# lとrのどちらかは全探索しても間に合う
for l in range(N + 1):
    # temp = left  +  middle     +  right
    # temp = l * L + (N - r) * R + (acc[r] - acc[l])

    # temp = (l * L - acc[l]) + ((N - r) * R + acc[r])
    temp = l_acc[l] + r_min[l]
    ans = min(ans, temp)
print(ans)
