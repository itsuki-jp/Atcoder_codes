T = int(input())
mod = 998244353
alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']
for _ in range(T):
    N = int(input())
    S = input()
    ans = 1
    for i in range(N):
        idx = alp.index(S[i])
        ans *= (idx)
