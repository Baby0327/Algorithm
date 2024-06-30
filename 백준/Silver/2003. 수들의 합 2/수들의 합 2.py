n, m = map(int, input().split())
num = list(map(int, input().split()))
num.append(0)

start = 0
end = 0
sum = num[start]
result = 0

while True:
    if sum > m:
        sum -= num[start]
        start += 1
    elif sum == m:
        result += 1
        end += 1
        sum += num[end]
        sum -= num[start]
        start += 1
    elif sum < m:
        end += 1
        if end >= n:
            break
        sum += num[end]

print(result)