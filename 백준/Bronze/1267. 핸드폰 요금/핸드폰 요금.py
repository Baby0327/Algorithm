input()
call = list(map(int, input().split()))
y, m = 0, 0

for i in call:
    y += 10 * (i // 30 + int(i % 30 >= 0))
    m += 15 * (i // 60 + int(i % 60 >= 0))

if y < m:
    print(f"Y {y}")
elif y > m:
    print(f"M {m}")
else:
    print(f"Y M {y}")