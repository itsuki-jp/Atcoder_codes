# CHR_Virtual_08
n = int(input())
s = set()
for _ in range(1, 2 * n + 2):
    s.add(_)
for _ in range(n + 1):
    print(s.pop(), flush=True)
    rm = int(input())
    if _ != n:
        s.remove(rm)
