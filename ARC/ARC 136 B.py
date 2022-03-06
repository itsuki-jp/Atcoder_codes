n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for _ in range(20):
    for i in range(n):
        if a[i] == b[i]:
            continue
        try:
            pos = a.index(b[i], i, n)
        except ValueError:
            break
        if n in (i + 1, i + 2):
            if a == b:
                exit(print("Yes"))
            else:
                break
        if i + 1 == pos:
            a[i], a[i + 1], a[i + 2] = a[i + 1], a[i + 2], a[i]
            continue
        a[i:pos + 1] = [b[i]] + a[i:pos]
        if (pos - i) % 2 == 1:
            a[i + 1], a[i + 2] = a[i + 2], a[i + 1]
        continue
if a == b:
    print("Yes")
else:
    print("No")
