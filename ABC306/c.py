n = int(input())
list_a = list(map(int, input().split()))

temp = [[-1, int(i) + 1] for i in range(n)]
cnt = [0] * n
for i in range(3 * n):
    num = list_a[i] - 1
    cnt[num] += 1
    if cnt[num] == 2:
        temp[num][0] = i
temp.sort()
ans = []
for ind, num in temp:
    ans.append(num)
print(*ans)
