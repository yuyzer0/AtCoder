n = int(input())
ans = "No"
list_s = []
for _ in range(n):
    list_s.append(str(input()))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        s = list_s[i] + list_s[j]
        ans = "No"
        for x in range(len(s)):
            y = len(s) - 1 - x
            if not (0 <= y <= len(s) - 1):
                break
            if s[x] == s[y]:
                ans = "Yes"
                continue
            else:
                ans = "No"
                break
        if ans == "Yes":
            print(ans)
            exit()
print("No")
