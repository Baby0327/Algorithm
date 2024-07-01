M, N = map(int, input().split())
snack = list(map(int, input().split()))

left = 1
right = max(snack)
result = 0
while left <= right:
    middle = (left + right)//2

    if middle == 0:
        result = 0
        break

    count = 0
    for i in snack:
        if i >= middle:
            count += (i//middle)
    if count >= M:
        left = middle + 1
        result = max(result, middle)
    else:
        right = middle - 1

print(result)