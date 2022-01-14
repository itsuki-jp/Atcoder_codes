s, t, x = map(int, input().split())
if s < t:
    ans = [i for i in range(s, t)]
else:
    ans = [i for i in range(s, 25)] + [i for i in range(t)]
if x in ans:
    print("Yes")
else:
    print("No")
