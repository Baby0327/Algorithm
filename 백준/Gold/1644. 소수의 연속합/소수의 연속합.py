n = int(input())
num = [True for i in range(n+1)]
num[0] = False
num[1] = False
prime = []
for i in range(n+1):
    if num[i]:
        prime.append(i)
        for j in range(i+i, n+1, +i):
            num[j] = False

end = 0
sum = 0
result = 0
for start in range(len(prime)):
    while sum < n and end < len(prime):
        sum += prime[end]
        end += 1
    if sum == n:
        result += 1
    sum -= prime[start]

print(result)