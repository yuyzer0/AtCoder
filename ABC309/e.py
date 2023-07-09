import heapq

n, m = map(int, input().split())
list_p = list(map(int, input().split()))
visited = [-1] * n
edge = [[] for _ in range(n)]
in_num = [0] * n

for i in range(n-1):
    child = i + 1
    p = list_p[i] - 1
    edge[p].append(child)
    in_num[child] += 1

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    if visited[x] < y:
        visited[x] = y

hq = []

for i in range(n):
    if in_num[i] == 0:
        heapq.heappush(hq, i)

cnt = 0
while len(hq) > 0:
    u = heapq.heappop(hq)
    now = visited[u]
    for v in edge[u]:
        in_num[v] -= 1
        if in_num[v] == 0:
            visited[v] = max(visited[v], now - 1)
            heapq.heappush(hq, v)
    if not (now == -1):
        cnt += 1

print(cnt)
