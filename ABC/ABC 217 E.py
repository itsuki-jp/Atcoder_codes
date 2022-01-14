import heapq
q = int(input())
lst = []
h = []
heapq.heapify(h)
for j in range(q):
    query = input()
    if int(query[0]) == 1:
        _, x = query.split()
        x = int(x)
        lst.append(x)
    elif int(query[0]) == 2:
        if len(h) != 0:
            print(heapq.heappop(h))
        else:
            print(lst.pop(0))
    else:
        for i in lst:
            heapq.heappush(h,i)
        lst = []
