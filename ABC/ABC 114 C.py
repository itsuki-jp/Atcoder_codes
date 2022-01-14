n = int(input())


def solve( num ):
    if int(num) > n:
        return 0
    ans = 1 if all(num.count(c) > 0 for c in "753") else 0
    for c in "753":
        ans += solve((num + c))
    return ans


print(solve("0"))
