import string
alphabet = string.ascii_uppercase

n = int(input())
s = list(input())
for i in range(len(s)):
    pos = alphabet.index(s[i]) + n
    if pos > 25:
        pos -= 26
    s[i] = alphabet[pos]
print("".join(s))