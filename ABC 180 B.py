n = int(input())
x = list(map(int, input().split()))
ans1 = 0
ans2 = 0
ans3 = 0
for i in x:
    ans1 += abs(i)
    ans2 += abs(i)**2
    ans3 = max(abs(i),ans3)
print(ans1)
print(ans2**0.5)
print(ans3)