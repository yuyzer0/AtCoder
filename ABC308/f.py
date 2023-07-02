import heapq


n, m = map(int, input().split())
list_p = list(map(int, input().split()))
ans = sum(list_p)
list_p.sort()

list_l = list(map(int, input().split()))
list_lef = []
for i in range(m):
    list_lef.append([list_l[i], i])
list_lef.sort(reverse=True)

list_d = list(map(int, input().split()))

hq = []
for i in range(n):
    # 値段が安い順
    price = list_p[i]
    while len(list_lef) > 0 and price >= list_lef[-1][0]:
        # 値段が高い順に並んでいるのを後ろから確認
        # クーポンが使える場合
        lef, li = list_lef.pop()
        heapq.heappush(hq, list_d[li] * -1)
    if len(hq) > 0:
        dis = heapq.heappop(hq) * -1
        ans -= dis

print(ans)
