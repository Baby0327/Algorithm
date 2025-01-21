n = int(input())
print("".join(str(i) for i in range(1, n + 1)).index(str(n)) + 1)