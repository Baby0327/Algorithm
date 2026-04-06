n = [int(input()) for _ in range(9)]
s = sum(n)

for i in range(9):
    for j in range(i + 1, 9):
        if s - n[i] - n[j] == 100:
            print("\n".join([str(n[k]) for k in range(9) if k not in [i, j]]))