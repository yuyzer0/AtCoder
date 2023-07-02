n, m = map(int, input().split())
list_c = list(map(str, input().split()))
list_d = [""] + list(map(str, input().split()))

list_p = list(map(int, input().split()))
price = dict()
for i in range(1, m+1):
    price[list_d[i]] = list_p[i]

ans = 0
for i in range(n):
    c = list_c[i]
    if price.get(c, -1) == -1:
        ans += list_p[0]
    else:
        ans += price[c]
print(ans)
