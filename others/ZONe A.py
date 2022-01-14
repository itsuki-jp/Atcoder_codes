a = list(input())
ans = 0
for i in range(12-3):
    temp = a[i:i+4]
    if a[i:i+4] == ['Z', 'O', 'N', 'e']:
        ans += 1

print(ans)
