n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)
ans = h[k:]
print(sum(ans))

