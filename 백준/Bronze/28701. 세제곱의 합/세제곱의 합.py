n = int(input())

result1 = 0
result2 = ((n*(n+1))//2)**2
result3 = 0

for i in range(1, n+1):
    result1 += i**1
    result3 += i**3

print(result1)
print(result2)
print(result3)