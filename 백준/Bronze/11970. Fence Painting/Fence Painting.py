n = [0] * 101

for _ in range(2):
    s, e = map(int, input().split())

    for i in range(s, e):
        n[i] = 1

print(n.count(1))