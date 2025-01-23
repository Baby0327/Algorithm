r, c = map(int, input().split())
s = [input() for _ in range(r)]
result = [0 for _ in range(5)]

for i in range(r - 1):
    for j in range(c - 1):
        temp = [s[i][j], s[i][j + 1], s[i + 1][j], s[i + 1][j + 1]]
        if temp.count("#") == 0:
            result[temp.count("X")] += 1

print("\n".join(list(map(str, result))))