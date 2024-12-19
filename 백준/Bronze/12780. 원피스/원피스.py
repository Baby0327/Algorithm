h = input()
n = input()
result = 0

for i in range(len(h) - len(n) + 1):
    if h[i:i + len(n)] == n:
        result += 1

print(result)