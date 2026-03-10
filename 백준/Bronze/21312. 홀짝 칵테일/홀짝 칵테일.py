n = list(map(int, input().split()))
result = [1, 1]
check = 0

for i in n:
    if i % 2:
        check = 1
        result[1] *= i
    else:
        result[0] *= i

print(result[1] if check or result[1] > 1 else result[0])