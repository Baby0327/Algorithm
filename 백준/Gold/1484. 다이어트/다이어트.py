g = int(input())
num = {}
result = []

for i in range(1, int(g**0.5) + 1):
    if g % i == 0 and i != g // i:
        num[i] = g // i

for k, v in num.items():
    temp = (k + v) / 2
    if temp.is_integer():
        result.append(int(temp))

print("\n".join(map(str, result[::-1])) if result else -1)