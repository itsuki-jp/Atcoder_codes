n = int(input())
s = [input() for _ in range(n)]


def ok( y, x ):
    if 0 <= y < n and 0 <= x < n:
        return True
    else:
        return False


for i in range(n):
    for j in range(n):
        if j <= n - 6:
            t1 = 0
            for k in range(j, j + 6):
                if s[i][k] == "#":
                    t1 += 1
            if t1 >= 4:
                exit(print("Yes"))

        if i <= n - 6:
            t2 = 0
            for k in range(i, i + 6):
                if s[k][j] == "#":
                    t2 += 1
            if t2 >= 4:
                exit(print("Yes"))

        t3 = 0
        cnt3 = 0
        for k in range(6):
            if ok(i + k, j + k):
                cnt3 += 1
                if s[i + k][j + k] == "#":
                    t3 += 1
            else:
                break
        if cnt3 == 6 and t3 >= 4:
            exit(print("Yes"))

        t4 = 0
        cnt4 = 0
        for k in range(6):
            if ok(i - k, j + k):
                cnt4 += 1
                if s[i - k][j + k] == "#":
                    t4 += 1
            else:
                break
        if cnt4 == 6 and t4 >= 4:
            exit(print("Yes"))
print("No")
