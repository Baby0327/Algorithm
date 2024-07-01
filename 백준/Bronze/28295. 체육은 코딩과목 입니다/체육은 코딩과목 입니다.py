now = 0
for i in range(10):
    t = int(input())
    if t == 1:
        now += 90
    elif t == 2:
        now += 180
    elif t == 3:
        now -= 90

if now % 360 == 0:
    print("N")
elif now % 360 == 90:
    print("E")
elif now % 360 == 180:
    print("S")
else:
    print("W")