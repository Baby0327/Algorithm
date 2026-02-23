n = int(input())
cnt = 0

for b in range(1, 500):
    a = (b**2 + n)**0.5
    
    if int(a) == a:
        cnt += 1

print(cnt)