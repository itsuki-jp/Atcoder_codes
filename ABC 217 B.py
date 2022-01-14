lst = ["ABC","ARC","AGC","AHC"]
for _ in range(3):
    s = input()
    lst.remove(s)
print(*lst)