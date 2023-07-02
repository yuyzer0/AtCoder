from collections import deque


h, w = map(int, input().split())
list_s = []
for _ in range(h):
    list_s.append(str(input()))

sx, sy = 0, 0
gx, gy = h-1, w-1

visited = [[-1] * w for _ in range(h)]

q = deque()
q.append([sx, sy])
visited[sx][sy] = 0

next_info = [[1, 0], [-1, 0], [0, -1], [0, 1]]

temp = "snuke"
moji = dict()
for i in range(len(temp)):
    c = temp[i]
    moji[c] = i

while len(q) > 0:
    sx, sy = q.popleft()
    for ax, ay in next_info:
        tx = sx + ax
        ty = sy + ay
        if not (0 <= tx < h) or not (0 <= ty < w):
            continue
        if not (visited[tx][ty] == -1):
            continue
        now = list_s[sx][sy]
        if moji.get(now, -1) == -1:
            continue
        nex = temp[(moji[now] + 1) % 5]
        if not (list_s[tx][ty] == nex):
            continue
        visited[tx][ty] = visited[sx][sy] + 1
        q.append([tx, ty])

if visited[gx][gy] == -1:
    print("No")
else:
    print("Yes")
