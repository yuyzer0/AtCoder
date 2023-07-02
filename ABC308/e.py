n = int(input())
list_a = list(map(int, input().split()))
s = str(input())
mex = "@MEX"

dp = [[[0] * (1 << 4) for _ in range(4)] for _ in range(n)]

if s[0] == "M":
    a = list_a[0]
    dp[0][1][1 << a] = 1

for i in range(n-1):
    for j in range(4):
        if j == 0 and s[i+1] == "M":
            a = list_a[i+1]
            dp[i+1][j+1][1 << a] += 1
        for k in range(1 << 4):
            # i文字
            dp[i+1][j][k] += dp[i][j][k]
            # i文字
            c = s[i+1]
            a = list_a[i+1]
            if j == 1 and c == "E":
                dp[i+1][j+1][k | 1 << a] += dp[i][j][k]
            elif j == 2 and c == "X":
                dp[i+1][j+1][k | 1 << a] += dp[i][j][k]

ans = 0
for k in range(1 << 4):
    num = dp[n-1][3][k]
    x = 0
    sk = format(k, "04b")
    for ind in range(4):
        if sk[ind] == "0":
            x = (3 - ind)
    ans += num * x

print(ans)
