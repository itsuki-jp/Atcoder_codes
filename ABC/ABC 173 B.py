n = int(input())
cnt = [0]*4
judge = ["AC", "WA", "TLE", "RE"]
for i in range(n):
    s = input()
    for j in range(4):
        if judge[j] == s:
            cnt[j] += 1
for k in range(4):
    print(judge[k], "x", cnt[k])
