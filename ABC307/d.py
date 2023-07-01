n = int(input())
s = str(input())
num = 0
temp = [[""]]
for c in s:
    if c == "(":
        num += 1
        temp.append([c])
    elif c == ")" and num > 0:
        num -= 1
        temp.pop()
    else:
        temp[num].append(c)

ans = []
for x in temp:
    for c in x:
        ans.append(c)
print("".join(ans))
