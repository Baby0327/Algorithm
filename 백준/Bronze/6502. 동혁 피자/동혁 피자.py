cnt = 1

while 1:
    n = list(map(int, input().split()))

    if n == [0]:
        break

    result = n[0] * 2 >= (n[1]**2 + n[2]**2)**0.5
    print(f"Pizza {cnt} {'fits' if result else 'does not fit'} on the table.")
    cnt += 1