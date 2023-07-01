import heapq

n, m = map(int, input().split())

edge = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append([v, w])
    edge[v].append([u, w])

k = int(input())
list_a = [int(i) - 1 for i in input().split()]

d = int(input())
list_x = list(map(int, input().split()))

ans = [-1] * n
hq = []
checked = [False] * n

for a in list_a:
    ans[a] = 0
    checked[a] = True
    for v, w in edge[a]:
        heapq.heappush(hq, [w, v])

for i in range(d):
    power = list_x[i]
    # 新規感染
    hq2 = []

    # 昨日までの感染者から
    while len(hq) > 0:
        dis, v = heapq.heappop(hq)
        if dis > power:
            heapq.heappush(hq, [dis, v])
            break
        elif ans[v] == -1:
            ans[v] = i + 1
            heapq.heappush(hq2, [(power - dis) * -1, v])

    # 新規感染者から
    while len(hq2) > 0:
        dis, u = heapq.heappop(hq2)
        dis *= -1
        if checked[u]:
            continue
        checked[u] = True
        for v, w in edge[u]:
            if ans[v] == -1 or ans[v] == i + 1:
                if w <= dis:
                    ans[v] = i + 1
                    heapq.heappush(hq2, [(dis - w) * -1, v])
                else:
                    heapq.heappush(hq, [w, v])

for out in ans:
    print(out)
