import sys
print = sys.stdout.write

def self(n):
    num = n

    for i in str(n):
        num += int(i)

    return num

result = [i for i in range(10001)]

for i in range(1, 10001):
    n = self(i)

    if n <= 10000:
        result[n] = 0

print("\n".join([str(i) for i in range(1, 10001) if result[i] != 0]))
