import sys
input = sys.stdin.readline

result = []

for i in range(int(input())):
    n, name, country = input().rstrip().split()
    if country == "Russia":
        result.append([int(n), name])

print(sorted(result, reverse=True)[0][1])