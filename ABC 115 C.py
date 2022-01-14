N,K = map(int,input().split())
h = [int(input()) for _ in range(N)]
h.sort()
max_min = h[K-1] - h[0]
check = int()
for i in range(1,N-K+1):
    check = h[i + K-1] - h[i]
    if check < max_min:
        max_min = check
print(max_min)