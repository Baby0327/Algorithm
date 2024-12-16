n = list(map(int, input().split()))
n[2] += 1

if n[2] >= 60:
    n[1] += n[2] // 60
    n[2] = n[2] % 60
if n[1] >= 60:
    n[0] += n[1] // 60
    n[1] = n[1] % 60
if n[0] >= 24:
    n[0] = n[0] % 24

print(":".join([str(i).zfill(2) for i in n]))