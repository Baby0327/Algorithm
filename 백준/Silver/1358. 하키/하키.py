W, H, X, Y, P = map(int, input().split())
count = 0

for i in range(P):
    a, b = map(int, input().split())
    if X <= a <= X+W and Y <= b <= Y+H:
        count += 1
    elif (X-a)**2 + (Y+H/2-b)**2 <= H**2/4:
        count += 1
    elif (X+W-a)**2 + (Y+H/2-b)**2 <= H**2/4:
        count += 1
    else:
        continue

print(count)