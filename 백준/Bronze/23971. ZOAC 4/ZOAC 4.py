h, w, n, m = map(int, input().split())
print((h // (n + 1) + int(h % (n + 1) > 0)) * (w // (m + 1) + int(w % (m + 1) > 0)))