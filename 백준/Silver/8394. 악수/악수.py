n = int(input())

result = [1, 2]

while len(result) < n:
    result.append((result[-1]%10 + result[-2]%10)%10)

print(result[-1])