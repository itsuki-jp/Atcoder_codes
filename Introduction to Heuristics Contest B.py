d = int(input())
#満足度の下がりやすさ
#
c = list(map(int,input().split()))
#d 日目にタイプ i のコンテストを開催した場合、満足度が sd,i 増加
s = [list(map(int,input().split())) for _ in range(d)]#
t = []
for i in range(d):
    t.append(int(input()))

