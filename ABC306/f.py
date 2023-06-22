class Fenwick_Tree:
    def __init__(self, n) -> None:
        self.size = n
        self.tree = [0] * (n+1)

    def sum(self, lef, rig) -> int:
        return self._sum(rig) - self._sum(lef)

    def _sum(self, i) -> int:
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x) -> None:
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


n, m = map(int, input().split())
list_a = []
pair = []
for i in range(n):
    temp = list(map(int, input().split()))
    list_a.append(temp)
    for j in range(m):
        pair.append([temp[j], i])
pair.sort()

ans = ((m+1) * m // 2) * (n * (n-1) // 2)

bit = Fenwick_Tree(n * m)
for num, ind in pair:
    bit.add(ind, 1)
    ans += bit.sum(ind+1, n)

print(ans)
