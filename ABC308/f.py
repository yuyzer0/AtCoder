import heapq
n, m = map(int, input().split())
list_p = list(map(int, input().split()))
ans = sum(list_p)
list_p.sort(reverse=True)

list_l = list(map(int, input().split()))
list_d = list(map(int, input().split()))

list_ld = []
for i in range(m):
    lef = list_l[i]
    dis = list_d[i] * -1
    list_ld.append([lef, dis])
list_ld.sort(reverse=True)

can_used = []
while len(list_p) > 0:
    price = list_p.pop()
    while len(list_ld) > 0:
        lef, dis = list_ld.pop()
        dis *= -1
        if price >= lef:
            heapq.heappush(can_used, dis * -1)
        else:
            list_ld.append([lef, dis * -1])
            break
    while len(can_used) > 0:
        ans -= heapq.heappop(can_used) * -1
        break

print(ans)
