X, Y = input().split()
X = list(X)
Y = list(Y)

X_reversed = "".join(reversed(X))
Y_reversed = "".join(reversed(Y))
tmp = str(int(X_reversed) + int(Y_reversed))
result = list(reversed(tmp))

i = 0
while result[i] == '0':
    del result[i]

print("".join(result))