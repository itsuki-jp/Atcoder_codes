n, h = map(int, input().split())
b_lst = []
a_max = 0
for _ in range(n):
    a, b = map(int, input().split())
    b_lst.append(b)
    a_max = max(a, a_max)
ans = 0
b_lst.sort(reverse=True)
for b in b_lst:
    if b >= a_max and h > 0:
        ans += 1
        h -= b
    else:
        break
if h > 0:
    ans += -(-h // a_max)
print(ans)
