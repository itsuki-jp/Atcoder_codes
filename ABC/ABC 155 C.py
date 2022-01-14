import collections
n = int(input())
s = [input() for _ in range(n)]
word = collections.Counter(s)
word = word.most_common()
max_num = word[0][1]
word.sort()
for i in range(len(word)):
    if word[i][1] == max_num:
        print(word[i][0])