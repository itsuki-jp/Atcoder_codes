def solve( ans, num ):
    if len(ans) == n:
        print(ans)
        return
    for c in range(num + 1):
        solve(ans + char[c], num)
    if len(ans) != 0:
        solve(ans + char[num + 1], num + 1)


n = int(input())
char = []
for i in range(97, 123):
    char.append(chr(i))
solve("", 0)
