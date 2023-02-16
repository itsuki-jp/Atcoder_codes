n = int(input())
a = [list(input()) for _ in range(n)]
ans = "correct"


def not_ok():
    global ans
    global tf
    ans = "incorrect"
    tf = False


for i in range(n):
    tf = True
    for j in range(i, n):
        if i == j:
            continue
        if a[i][j] == a[j][i] == "D":
            continue
        elif "D" in [a[i][j], a[j][i]]:
            not_ok()
            break
        elif a[i][j] == a[j][i]:
            not_ok()
            break
    if not tf:
        break
print(ans)
