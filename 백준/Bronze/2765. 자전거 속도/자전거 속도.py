n = 1

while 1:
    r, s, t = map(float, input().split())

    if s == 0:
        break

    d = (r * 3.1415927) / 63360 * s
    print(f"Trip #{n}: {d:.2f} {d / (t / 3600):.2f}")
    n += 1