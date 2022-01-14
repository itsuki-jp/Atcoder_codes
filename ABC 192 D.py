def henkan( list, shinsu ):
    l = len(list)
    ans = 0
    for i in range(1, l + 1):
        ans += list[-i] * (shinsu ** (i - 1))
    return ans


def binary_search( array, item,cnt ):
    head = 0
    tail = 10**30

    while head <= tail:
        num = henkan(array,cnt)
        center = (head + tail) // 2
        if num > item:
            return cnt
        elif array[center] < item:
            head = center + 1
        else:
            tail = center - 1

    return None


x = int(input())
m = int(input())
ans = 0
x = [int(i) for i in str(x)]
cnt = max(x) + 1
binary_search(x,m,cnt)