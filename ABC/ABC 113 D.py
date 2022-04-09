n = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(n)]
ans[0] = sum([A[_] for _ in range(0, n, 2)]) - sum([A[_] for _ in range(1, n, 2)])
A[0] -= ans[0] // 2
A[-1] -= ans[0] // 2
for i in range(1, n):
    ans[i] = A[i - 1] * 2
    A[i] -= A[i - 1]
print(*ans)
