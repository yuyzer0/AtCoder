n = int(input())
list_a = list(map(int, input().split()))
ans = [0] * n
now = 0
cnt = 1
for a in list_a:
    ans[now] += a
    cnt += 1
    if cnt > 7:
        cnt = 1
        now += 1
print(*ans)
