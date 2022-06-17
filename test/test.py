from collections import defaultdict

sets = set()
word_id = defaultdict(int)
num_doc = 1500
num_word = 12419
n = 0
tf = [[0 for _ in range(num_doc)] for _ in range(num_word)]
while True:
    a = input()
    if a == "":
        break
    sets.add(a)
    n += 1
print(len(sets))
print(n)
