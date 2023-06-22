list_a = map(int, input().split())
ans = 0
x = 1
for a in list_a:
    ans += a * x
    x *= 2
print(ans)
