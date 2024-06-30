count = [0 for i in range(42)]

for i in range(10):
    N = int(input())
    count[N%42] += 1

result = 0
for i in count:
    if i != 0:
        result += 1

print(result)