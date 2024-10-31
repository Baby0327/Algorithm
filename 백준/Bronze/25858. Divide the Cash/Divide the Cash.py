n, d = map(int, input().split())
s = []

for i in range(n):
    s.append(int(input()))

print("\n".join(list(map(str, [i * (d//sum(s)) for i in s]))))