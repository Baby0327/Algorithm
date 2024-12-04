p, r = map(int, input().split())
result = p / r

if result < 0.2:
    print("weak")
elif result < 0.4:
    print("normal")
elif result < 0.6:
    print("strong")
else:
    print("very strong")