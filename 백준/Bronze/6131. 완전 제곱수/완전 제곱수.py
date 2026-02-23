n = int(input())
cnt = 0

for b in range(1, 501):
    for a in range(b, 501):
        if a**2 == b**2 + n:
            cnt += 1
            break

print(cnt)