from collections import Counter

s = input()
t = input()
n = len(s)
dict = {}
for i in range(n):
    if s[i] in dict and (dict[s[i]] != t[i]) or (t[i] in dict.values() and (s[i], t[i]) not in dict.items()):
        print("No")
        exit()
    if s[i] not in dict:
        dict[s[i]] = t[i]
print("Yes")
