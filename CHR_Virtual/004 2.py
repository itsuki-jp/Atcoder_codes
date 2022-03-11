def dist( p1, p2, arr ):
    return [max(abs(arr[p1][0] - arr[p2][0]), abs(arr[p1][1] - arr[p2][1]))
        , (max(arr[p1][2], arr[p2][2]), min(arr[p1][2], arr[p2][2]))]


n = int(input())
xy = []
yx = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    xy.append([x, y, _])
    yx.append([y, x, _])
xy.sort()
yx.sort()
ans = [dist(0, -1, xy), dist(0, -2, xy), dist(1, -1, xy), dist(0, -1, yx), dist(0, -2, yx), dist(1, -1, yx)]
ans.sort(reverse=True)
s = set()
s.add(ans[0][1])
for i in range(1, len(ans) - 1):
    if ans[i][1] not in s:
        print(ans[i][0])
        exit()
    else:
        s.add(ans[i][1])
