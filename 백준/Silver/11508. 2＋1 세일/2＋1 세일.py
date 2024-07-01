import sys

n = int(sys.stdin.readline())
product = []
for i in range(n):
    product.append(int(sys.stdin.readline()))

product.sort(reverse=True)
result = 0
for i in range(n):
    if i % 3 != 2:
        result += product[i]

print(result)