# https://note.nkmk.me/python-union-find/
from collections import defaultdict


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


h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
tate = UnionFind(h * w * 10)
yoko = UnionFind(h * w * 10)

# yoko
for i in range(h):
    for j in range(w - 1):
        if s[i][j] == s[i][j + 1] == ".":
            yoko.union(w * i + j, w * i + j + 1)
# tate
for j in range(w):
    for i in range(h - 1):
        if s[i][j] == s[i + 1][j] == ".":
            tate.union(w * i + j, w * (i + 1) + j)
ans = 0
for i in range(h * w + 1):
    tt = tate.size(i)
    yy = yoko.size(i)
    temp = tate.size(i) + yoko.size(i)
    ans = max(ans, temp)
print(ans - 1)
