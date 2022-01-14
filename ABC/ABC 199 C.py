n = int(input())
s = list(input())
q = int(input())
first, second = s[:n], s[n:]
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        a -= 1
        b -= 1
        if b < n:
            first[a], first[b] = first[b], first[a]
        elif n <= a:
            second[a-n], second[b-n] = second[b-n], second[a-n]
        else:
            first[a], second[b - n] = second[b - n], first[a]
    else:
        first, second = second, first
print(''.join(first + second))
