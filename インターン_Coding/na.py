import sys
from collections import deque
from collections import defaultdict

# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

T = TypeVar('T')


class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build( self, a=None ) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size: size * (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__( self, a: Iterable[T] = [] ) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__( self ) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__( self ) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j

    def __len__( self ) -> int:
        return self.size

    def __repr__( self ) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__( self ) -> str:
        s = str(list(self))
        return "{" + s[1: len(s) - 1] + "}"

    def _find_bucket( self, x: T ) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]: return a
        return a

    def __contains__( self, x: T ) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count( self, x: T ) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add( self, x: T ) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard( self, x: T ) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True

    def lt( self, x: T ) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le( self, x: T ) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt( self, x: T ) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge( self, x: T ) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__( self, x: int ) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError

    def index( self, x: T ) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right( self, x: T ) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


def step1( lines ):
    idx = 0
    M = int(lines[idx])
    idx += 1
    dct = {}
    for _ in range(M):
        D, S, P = map(int, lines[idx].split())
        idx += 1
        dct[D] = [S, P]  # 在庫、価格
    for _ in range(len(lines) - M - 1):
        temp = lines[idx].split()
        idx += 1
        [T, D, N] = [int(__) for __ in temp[1:]]
        if dct[D][0] >= N:
            dct[D][0] -= N
            for i in range(N):
                print(f"received order {T} {D}")
        else:
            print(f"sold out {T}")


def step2( lines ):
    idx = 0
    M, K = map(int, lines[idx].split())
    idx += 1
    dct = {}
    for _ in range(M):
        D, S, P = map(int, lines[idx].split())
        idx += 1
        dct[D] = [S, P]  # 在庫、価格
    d = deque()
    in_use = SortedMultiset()
    for _ in range(len(lines) - M - 1):
        temp = lines[idx].split()
        idx += 1
        if temp[0] == "received":
            [T, D] = [int(__) for __ in temp[2:]]
            if len(in_use) < K:
                in_use.add(D)
                print(D)
            else:
                d.append(D)
                print("wait")
        else:
            D = int(temp[1])
            if D in in_use:
                if len(d) != 0:
                    nxt = d.popleft()
                    in_use.add(nxt)
                    print(f"ok {nxt}")
                else:
                    print(f"ok")
                in_use.discard(D)
            else:
                print("unexpected input")


def step3( lines ):
    idx = 0
    M = int(lines[idx])
    idx += 1
    dct = {}
    for _ in range(M):
        D, S, P = map(int, lines[idx].split())
        idx += 1
        dct[D] = [S, P]  # 在庫、価格

    in_use = defaultdict(int)
    for _ in range(len(lines) - M - 1):
        temp = lines[idx].split()
        idx += 1
        if temp[0] == "received":
            [T, D] = [int(__) for __ in temp[2:]]
            if in_use[D] == 0:
                in_use[D] = deque()
            in_use[D].append(T)
        else:
            D = int(temp[1])
            now = in_use[D].popleft()
            if len(in_use[D]) == 0:
                in_use[D] = 0
            print(f"ready {now} {D}")


def step4( lines ):
    idx = 0
    M = int(lines[idx])
    idx += 1
    dct = {}
    for _ in range(M):
        D, S, P = map(int, lines[idx].split())
        idx += 1
        dct[D] = [S, P]  # 在庫、価格

    table_info = defaultdict(int)
    total = defaultdict(int)
    for _ in range(len(lines) - M - 1):
        temp = lines[idx].split()
        idx += 1
        if temp[0] == "received":
            [T, D] = [int(__) for __ in temp[2:]]
            if table_info[T] == 0:
                table_info[T] = SortedMultiset()
            table_info[T].add(D)
            total[T] += dct[D][1]
        elif temp[0] == "ready":
            [T, D] = [int(__) for __ in temp[1:]]
            table_info[T].discard(D)
            if (len(table_info[T]) == 0):
                table_info[T] = 0
        elif temp[0] == "check":
            T = int(temp[1])
            if table_info[T] == 0:
                print(total[T])
                total[T] = 0
                table_info[T] = 0
            else:
                print("please wait")
    pass


def main( lines ):
    if lines[0] == "1":
        step1(lines[1:])
    if lines[0] == "2":
        step2(lines[1:])
    if lines[0] == "3":
        step3(lines[1:])
    if lines[0] == "4":
        step4(lines[1:])


def test():
    lines = []
    with open("input.txt") as f:
        for s_line in f:
            lines.append(s_line.rstrip('\r\n'))
    return lines


def real():
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    return lines


if __name__ == '__main__':
    main(test())
