N = int(input())

result = []

for i in range(N):
    line = list(input())
    left = 0
    right = 0
    for j in line:
        if j == '(':
            left += 1
        else:
            right += 1
        if right > left:
            result.append('NO')
            break
    if left == right:
        result.append('YES')
    elif left > right:
        result.append('NO')

for i in result:
    print(i)