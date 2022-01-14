n,k = map(int,input().split())
a = list(map(int,input().split()))
import collections
c = collections.Counter(a).most_common()[::-1]
l = len(set(a))
ans = 0
cnt = 0
while l > k:
  ans += c[cnt][1]
  cnt += 1
  l -= 1
print(ans)