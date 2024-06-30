n = int(input())

sum = 0
end = 1
result = 0
for start in range(1, n+1):
    while end <= n and sum < n:
        sum += end
        end += 1

    if sum == n:
        result += 1
    sum -= start

print(result)