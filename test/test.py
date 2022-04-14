N, K = map(int, input().split())
a = list(map(int, input().split()))
A = [0] * N
A[0] = a[0]
for i in range(1, N):
    A[i] = A[i - 1] + a[i]  # A[i] は a[0] から a[i] までの和
A = [0] + A

ans = 0
for i in range(N):  # 各iに対して、A[right]-A[i-1] >= K となる最小のrightを二分探索で探して、ans += (N-right+1)    O(NlogN)
    left = i  # (a[i]からa[mid]までの和) >= K
    right = N
    mid = 0
    while not left == right:
        mid = (left + right) // 2
        if A[mid + 1] - A[i] >= K:
            right = mid
        else:
            left = mid + 1

    ans += N - right + 1

print(ans)
