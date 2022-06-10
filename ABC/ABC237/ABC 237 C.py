s = input()
rev = s[::-1]
n = len(s)
for _ in range(n + 1):
    if s == rev:
        exit(print("Yes"))
    s = "a" + s
    rev += "a"
print("No")