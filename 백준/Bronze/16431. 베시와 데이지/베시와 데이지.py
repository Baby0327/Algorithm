b1, b2 = map(int, input().split())
d1, d2 = map(int, input().split())
j1, j2 = map(int, input().split())
s1 = abs(d1 - j1) + abs(d2 - j2)
s2 = max(abs(b1 - j1), abs(b2 - j2))

if s1 > s2:
    print("bessie")
elif s1 < s2:
    print("daisy")
else:
    print("tie")