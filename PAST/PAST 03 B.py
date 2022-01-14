n, m, q = map(int, input().split())
problem = [n] * n
each_score = [[0] * m for _ in range(n)]
for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        s_score = each_score[s[1] - 1]
        ans = 0
        for j, k in zip(s_score, problem):
            if j != 0:
                ans += k
        print(ans)
    else:
        s_n = s[1] - 1
        s_m = s[2] - 1
        problem[s_m] -= 1
        each_score[s_n][s_m] = problem[s_m]