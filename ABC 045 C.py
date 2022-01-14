s = input()
n = len(s)


def dfs( i, j, k):
    if i >= n:
        return j + int(k)
    return dfs(i + 1, j + int(k), s[i]) + dfs(i + 1, j, k + s[i])


print(dfs(1, 0, s[0]))
