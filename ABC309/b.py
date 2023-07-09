import copy

n = int(input())
list_a = []
list_b = []
for _ in range(n):
    s = list(str(input()))
    list_a.append(s)

list_b = copy.deepcopy(list_a)

chg = set()
x = 0
y = 0
chg.add((x, y))

nx, ny = 0, 1
while True:
    a = list_a[x][y]
    if x == 0 and y == n - 1:
        nx = 1
        ny = 0
    elif x == n - 1 and y == n - 1:
        nx = 0
        ny = -1
    elif x == n - 1 and y == 0:
        nx = -1
        ny = 0
    x += nx
    y += ny
    list_b[x][y] = a
    if (x, y) in chg:
        break
    else:
        chg.add((x, y))

for b in list_b:
    print("".join(b))
