n = int(input())
check = 0
cnt = 1

while n > 1:
    if n % 2:
        check = 1
        n = (n + 1) // 2
    else:
        n //= 2
        if check:
            cnt += 1

print(cnt)