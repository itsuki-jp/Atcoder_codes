# https://note.nkmk.me/python-union-find/
from collections import defaultdict
import math


def combinations_count( n, r ):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


class UnionFind:
    def __init__( self, n ):
        self.n = n
        self.parents = [-1] * n

    def find( self, x ):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union( self, x, y ):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size( self, x ):
        return -self.parents[self.find(x)]

    def same( self, x, y ):
        return self.find(x) == self.find(y)

    def members( self, x ):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots( self ):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count( self ):
        return len(self.roots())

    def all_group_members( self ):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def max_size( self ):
        lst = list(self.all_group_members().values())
        res = 0
        for i in lst:
            res = max(res, len(i))
        return res

    def __str__( self ):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)][::-1]
uf = UnionFind(n + 1)
res = combinations_count(n, 2)
ans = []
for a, b in ab:
    ans.append(res)
    if uf.same(a, b):
        continue
    else:
        res -= uf.size(a) * uf.size(b)
        uf.union(a, b)
print(*ans[::-1], sep="\n")
