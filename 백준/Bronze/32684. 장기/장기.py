p = [13, 7, 5, 3, 3, 2]
c = sum(i * j for i, j in zip(p, list(map(int, input().split()))))
e = sum(i * j for i, j in zip(p, list(map(int, input().split())))) + 1.5
print("cocjr0208" if c > e else "ekwoo")