list_s = list(map(int, input().split()))

ans = "Yes"
pre = -1
for s in list_s:
    if not (pre <= s):
        ans = "No"
    if not (100 <= s <= 675):
        ans = "No"
    if not (s % 25 == 0):
        ans = "No"
    pre = s
print(ans)
