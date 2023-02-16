s = list(input())
for _ in range(3):
    if s.count(s[_]) == 1:
        print(s[_])
        exit()
print(-1)
