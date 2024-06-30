n = int(input())
drink = []

for i in range(n):
    drink.append(int(input()))

result = [0, drink[0], sum(drink[:2])]
for i in range(2, n):
    result.append(max(result[-2] + drink[i], result[-3] + drink[i-1] + drink[i], result[-1]))

print(result[n])