n, a, b = map(int, input().split())
ans = []
for y in range(n):
    for _ in range(a):
        temp = ""
        for x in range(n):
            if (x + y) % 2 == 0:
                temp += "." * b
            else:
                temp += "#" * b
        ans.append(temp)
print(*ans, sep="\n")
