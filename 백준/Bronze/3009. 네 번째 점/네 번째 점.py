X_list = []
Y_list = []

for i in range(3):
    X, Y = map(int, input().split())
    X_list.append(X)
    Y_list.append(Y)

X_list.sort()
Y_list.sort()

if X_list[1] != X_list[0]:
    X = X_list[0]
else:
    X = X_list[2]
if Y_list[1] != Y_list[0]:
    Y = Y_list[0]
else:
    Y = Y_list[2]

print(X,Y)