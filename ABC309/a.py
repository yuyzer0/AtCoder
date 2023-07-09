a, b = map(int, input().split())
ans = "No"
if b - 1 == a and not (a % 3 == 0):
    ans = "Yes"
print(ans)
