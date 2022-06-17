from math import log2
import csv

num_doc = 1500
num_word = 12419
n = 0


tf = [[0 for _ in range(num_doc)] for _ in range(num_word)]
path_docword = "docword.nips.txt"
docword_list = []
df = [0 for _ in range(num_word)]
with open(path_docword) as f:
    for s_line in f:
        s_line = [int(_) for _ in s_line[:-1].split()]
        tf[s_line[1] - 1][s_line[0] - 1] += s_line[2]
        df[s_line[1] - 1] += 1
        docword_list.append(s_line)

path_vocab = "vocab.nips.txt"
vobab_list = []
with open(path_vocab) as f:
    for s_line in f:
        s_line = s_line[:-1]
        vobab_list.append(s_line)

w = [[0 for _ in range(num_doc)] for _ in range(num_word)]
idf = [0 for _ in range(num_word)]
for i in range(num_word):
    idf[i] = log2(num_doc / df[i]) if df[i] != 0 else 0
    for j in range(num_doc):
        w[i][j] = tf[i][j] * idf[i]
num = 100
wi = []
for i in range(num_word):
    wi.append((sum(w[i]), i))
wi = sorted(wi, reverse=True)[:num]
ans = []
with open('ans.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    for a in range(num - 1):
        for b in range(a + 1, num):
            top = 0
            left = 0
            right = 0
            for i in range(num_doc):
                top += w[wi[a][1]][i] * w[wi[b][1]][i]
                left += w[wi[a][1]][i] ** 2
                right += w[wi[b][1]][i] ** 2
            value = top / (left ** 0.5 * right ** 0.5)
            ans.append([value, vobab_list[wi[a][1]], vobab_list[wi[b][1]]])
            writer.writerow([vobab_list[wi[a][1]], vobab_list[wi[b][1]], value])

ans.sort(reverse=True)
label_dct = {}
label = []
label_cnt = 0
with open('link_node.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    for i in ans:
        a = i[1]
        if a not in label_dct:
            label_dct[a] = label_cnt
            label.append(a)
            label_cnt += 1
        a = label_dct[i[1]]

        b = i[2]
        if b not in label_dct:
            label_dct[b] = label_cnt
            label.append(b)
            label_cnt += 1
        b = label_dct[b]

        if i[0] < 0.4:
            break
        writer.writerow(i + [a, b])
with open("label.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for i in label:
        writer.writerow([i])
