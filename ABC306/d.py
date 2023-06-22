n = int(input())

list_xy = []
for _ in range(n):
    x, y = map(int, input().split())
    list_xy.append([x, y])

visited = [[-1] * 2 for _ in range(n)]
ind, hara = 0, 0

if list_xy[0][0] == 0:
    visited[0][0] = max(0, list_xy[0][1])
else:
    visited[0][1] = max(0, list_xy[0][1])
    visited[0][0] = 0

for i in range(n-1):
    for j in range(2):
        now = visited[i][j]
        if now == -1:
            continue
        x, y = list_xy[i+1]
        if x == 0 and j == 0:
            visited[i+1][0] = max(visited[i+1][0], now + y, now)
        elif x == 1 and j == 0:
            visited[i+1][0] = max(visited[i+1][0], now)
            visited[i+1][1] = max(visited[i+1][1], now + y)
        elif x == 0 and j == 1:
            visited[i+1][0] = max(visited[i+1][0], now + y)
            visited[i+1][1] = max(visited[i+1][1], now)
        else:
            visited[i+1][0] = max(visited[i+1][0], 0)
            visited[i+1][1] = max(visited[i+1][1], now)

print(max(visited[n-1]))
