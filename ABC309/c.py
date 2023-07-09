n, k = map(int, input().split())
num = 0
list_ab = []
for _ in range(n):
    a, b = map(int, input().split())
    num += b
    list_ab.append([a, b])
list_ab.sort()

day = 0

if num <= k:
    print(1)
    exit()

for a, b in list_ab:
    num -= b
    day = a + 1
    if num <= k:
        break
print(day)
