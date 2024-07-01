n = int(input())
d = 0
p = 0

for i in range(n):
    tmp = input()
    if tmp == "D":
        d += 1
    elif tmp == "P":
        p += 1
    if max(d, p) - min(d, p) == 2:
        break
        
print(f"{d}:{p}")