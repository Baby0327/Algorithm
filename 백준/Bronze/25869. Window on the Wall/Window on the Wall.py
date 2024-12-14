w, h, d = map(int, input().split())
print((w - 2 * d) * (h - 2 * d) if w >= 2 * d and h >= 2 * d else 0)