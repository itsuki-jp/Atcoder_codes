from itertools import permutations


def main():
    n = int(input())
    lst = [[-1 for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]
    c = dict()
    for _ in range(2 * n - 1):
        a = list(map(int, input().split()))[::-1]
        for __ in range(len(a)):
            c[(_, 2 * n - 1 - __)] = a[__]
            c[(2 * n - 1 - __, _)] = a[__]
    ans = -1
    for i in permutations(range(2 * n)):
        temp = 0
        for j in range(n):
            x, y = i[2 * j], i[2 * j + 1]
            temp ^= c[(x, y)]
        if temp > ans:
            ans = temp
    print(ans)


if __name__ == '__main__':
    main()
