n, h, w = map(int, input().split())
s = ["?"] * n

for _ in range(h):
    l = input()

    for i in range(n):
        for j in range(w):
            if l[i*w + j] != "?":
                s[i] = l[i*w + j]
                break

print(*s, sep="")