N = int(input())

result = [0 for i in range(N+1)]
result[0] = 4

for i in range(1, N+1):
    result[i] = (int(result[i-1]**(1/2))*2 -1)**2

print(result[-1])