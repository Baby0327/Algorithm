a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())
print(max(max(a, c, e, g) - min(a, c, e, g), max(b, d, f, h) - min(b, d, f, h))**2)