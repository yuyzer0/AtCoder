n, m = map(int, input().split())
mod = 998244353

dp = [[0] * 2 for _ in range(n)]

dp[0][0] = 1

for i in range(n-1):
    dp[i+1][0] = dp[i][1] % mod
    dp[i+1][1] = dp[i][0] * (m-1) + dp[i][1] * (m-2) % mod

print(m * dp[-1][1] % mod)
