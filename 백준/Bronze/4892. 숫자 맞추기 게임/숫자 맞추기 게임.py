cnt = 0

while 1:
    n = int(input())

    if n == 0:
        break

    cnt += 1
    print(f"{cnt}. {'odd' if n % 2 else 'even'} {(3 * n + 1) // 6}")