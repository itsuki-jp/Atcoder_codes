def solve( n ):
    if n == 1:
        return "1"
    if S[n - 1] == -1:
        S[n - 1] = solve(n - 1)
    return f"{S[n - 1]} {n} {S[n - 1]}"


N = int(input())
S = [-1 for _ in range(30)]
ans = solve(N)
print(ans)
