n = list(map(int, input().split()))
i = 0

while max(n) < 5:
    if i % 2:
        n[0] += n[1]
    else:
        n[1] += n[0]
    i += 1

print("yt" if n[0] < n[1] else "yj")