N, Q = map(int, input().split())
a = [0] + list(map(int, input().split()))
lst = []
# aに含まれてない数字の配列を作る、多分遅い
for i in range(1, N + 1):
    lst.extend(list(range(a[i - 1] + 1, a[i])))
length = len(lst)

for _ in range(Q):
    k = int(input())
    if k <= length:
        print(lst[k - 1])
    else:
        print(a[-1] + k - length)
