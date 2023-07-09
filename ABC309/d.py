from collections import deque


n1, n2, m = map(int, input().split())
edge = [[] for _ in range(n1 + n2)]
visited = [-1] * (n1 + n2)
num1, num2 = 0, 0


for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)


visited[0] = 0
q = deque()
q.append(0)

while len(q) > 0:
    u = q.popleft()
    for v in edge[u]:
        if visited[v] == -1:
            visited[v] = visited[u] + 1
            num1 = max(num1, visited[v])
            q.append(v)

q = deque()
q.append(n1 + n2 - 1)
visited[n1 + n2 - 1] = 0
while len(q) > 0:
    u = q.popleft()
    for v in edge[u]:
        if visited[v] == -1:
            visited[v] = visited[u] + 1
            num2 = max(num2, visited[v])
            q.append(v)

print(num1 + num2 + 1)
