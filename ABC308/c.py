n = int(input())
list_a = []
list_b = []

for i in range(n):
    a, b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)

temp = [int(i) + 1 for i in range(n)]


class Frac:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a


temp = sorted(temp, key=lambda i:
              Frac(list_a[i-1] * -1, list_a[i-1] + list_b[i-1]))
print(" ".join(map(str, temp)))
