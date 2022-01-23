from itertools import permutations


def main():
    n = int(input())
    lst = [[-1 for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]
    for _ in range(2 * n - 1):
        a = list(map(int, input().split()))[::-1]
        for __ in range(len(a)):
            lst[_][-__ - 1] = a[__]
    ans = -1
    for i in permutations(range(2 * n)):
        temp = 0
        for j in range(n):
            x, y = i[2 * j], i[2 * j + 1]
            if not x > y:
                x, y = y, x
            temp ^= lst[y][x - 1]
        if temp > ans:
            ans = temp
    print(ans)


if __name__ == '__main__':
    main()
