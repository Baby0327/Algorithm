N = input()
N = list(map(int, N))

test = 0
for i in range(len(N) - 1, 0, -1):
    if N[i] >= 5:
        N[i - 1] += 1
        N[i] = 0
    else:
        N[i] = 0

result = "".join(map(str, N))
print(result)