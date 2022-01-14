import collections
n = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)
c_value = list(c.values())
c_key = list(c.keys())
cnt = 0

for i in range(len(c_key)):
    if c_key[i] > c_value[i]:
        cnt += c_value[i]
    elif c_value[i] > c_key[i]:
        cnt += c_value[i]- c_key[i]
print(cnt)