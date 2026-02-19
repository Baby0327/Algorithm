n = int(input())
temp = n % 8
result = 0

if temp > 4:
    result = 10 - temp
elif temp > 0:
    result = temp
else:
    result = 2

print(result)