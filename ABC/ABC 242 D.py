import sys


def solve( t, k ):
    c = {"A": "ABC", "B": "BCA", "C": "CAB"}
    if t == 0:
        return s[k]
    if k == 0:
        return c[s[0]][t % 3]
    char = solve(t - 1, k // 2)

    if k % 2 == 1:
        return c[char][2]
    else:
        return c[char][1]


input = sys.stdin.readline
s = input()
q = int(input())
for _ in range(q):
    T, K = map(int, input().split())
    print(solve(T, K - 1))
