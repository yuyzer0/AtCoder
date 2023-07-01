ha, wa = map(int, input().split())
list_a = []
a_kuro = []
for i in range(ha):
    list_a.append(str(input()))
    for j in range(wa):
        if list_a[i][j] == "#":
            a_kuro.append([i, j])

hb, wb = map(int, input().split())
list_b = []
b_kuro = []
for i in range(hb):
    list_b.append(str(input()))
    for j in range(wb):
        if list_b[i][j] == "#":
            b_kuro.append([i, j])

hx, wx = map(int, input().split())
list_x = []
x_kuro = []
temp = dict()
for i in range(hx):
    list_x.append(str(input()))
    for j in range(wx):
        if list_x[i][j] == "#":
            x_kuro.append([i, j])
            temp[(i, j)] = len(x_kuro) - 1

num = len(x_kuro)
for i in range(num):
    for j in range(num):
        dax = (a_kuro[0][0] - x_kuro[i][0]) * -1
        day = (a_kuro[0][1] - x_kuro[i][1]) * -1
        dbx = (b_kuro[0][0] - x_kuro[j][0]) * -1
        dby = (b_kuro[0][1] - x_kuro[j][1]) * -1
        ok = [False] * num
        # aを順に探索
        a_flg = True
        for k in range(len(a_kuro)):
            ax = a_kuro[k][0] + dax
            ay = a_kuro[k][1] + day
            if temp.get((ax, ay), -1) == -1:
                a_flg = False
            else:
                ind = temp[(ax, ay)]
                ok[ind] = True
        # bを順に探索
        b_flg = True
        for k in range(len(b_kuro)):
            bx = b_kuro[k][0] + dbx
            by = b_kuro[k][1] + dby
            if temp.get((bx, by), -1) == -1:
                b_flg = False
            else:
                ind = temp[(bx, by)]
                ok[ind] = True
        if ok.count(False) == 0 and a_flg and b_flg:
            print("Yes")
            exit()

print("No")
