from collections import deque

while True:
    n = int(input())
    if n == 0:
        break
    cards = [list(map(int, input().split())) for _ in range(n)]
    d = deque()
    for _ in range(n):
        if cards[_][0] != cards[_][1]:
            d.append(_)
    if len(d) == 0:
        print(0)
        continue
    d.append(d.popleft())
    ans = 0
    while len(d) != 0:
        ans += 1
        now = d.popleft()
        pre = d.pop()
        min_card = min(cards[pre])
        cards[pre].remove(min_card)
        if min_card in cards[now]:
            cards[now].remove(min_card)
        else:
            cards[now].append(min_card)
        if len(cards[pre]) != 0:
            d.append(pre)
        if len(cards[now]) != 0:
            d.append(now)
    print(ans)
