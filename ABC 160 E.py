x, y, a, b, c = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = sorted(list(map(int, input().split())), reverse=True)[:min(x + y, c)]

ans = p[:x] + q[:y] + r
ans.sort(reverse=True)
print(sum(ans[:x + y]))