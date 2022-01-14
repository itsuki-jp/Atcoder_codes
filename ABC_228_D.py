import sys

sys.setrecursionlimit(10 ** 9)


class UnionFind:
    def __init__( self, n ):
        self.parents = [-1] * n

    def root( self, x ):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def union( self, x, y ):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        self.parents[y] += self.parents[x]
        self.parents[x] = y


mod = 2 ** 20
uf = UnionFind(mod)
lst = [-1] * mod

q = int(input())
tx = [list(map(int, input().split())) for _ in range(q)]
for t, x in tx:
    if t == 1:
        now = x % mod
        while True:
            if lst[now] == -1:
                lst[now] = x
                uf.union(now, (now + 1) % mod)
                break
            else:
                now = uf.root(now)
    else:
        print(lst[x % mod])
