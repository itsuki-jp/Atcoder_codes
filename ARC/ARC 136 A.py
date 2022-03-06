n = int(input())
s = list(input())
pos = 0
while pos < n:
    if s[pos] == "B" and pos + 1 < n:
        if s[pos + 1] == "A":
            s[pos], s[pos + 1] = "A", "B"
        elif s[pos + 1] == "B":
            s[pos], s[pos + 1] = "", "A"
    pos += 1
print(*s, sep="")
