k = int(input())
s = input()
t = input()

usable = [0] + [k for _ in range(9)]
ss = 0
for i in range(1, 10):
    ss += i * 10 ** s.count(str(i))
    if s.count(str(i)) != 0:
        usable[i] -= s.count(str(i))
st = 0
for i in range(1, 10):
    st += i * 10 ** t.count(str(i))
    if t.count(str(i)) != 0:
        usable[i] -= t.count(str(i))
ans = 0
for i in range(1, 10):
    if usable[i] > 0:
        for j in range(1, 10):
            if i == j and usable[i] > 1:
                if ss - i * 10 ** s.count(str(i)) + i * 10 ** (s.count(str(i)) + 1) > st - j * 10 ** t.count(str(j)) + j * 10 ** (t.count(str(j)) + 1):
                    ans += usable[i] * (usable[i] - 1)
            if i != j and usable[j] > 0:
                if ss - i * 10 ** s.count(str(i)) + i * 10 ** (s.count(str(i)) + 1) > st - j * 10 ** t.count(str(j)) + j * 10 ** (t.count(str(j)) + 1):
                    ans += usable[i]*usable[j]
print(ans / ((9 * k - 8) * (9 * k - 9)))
