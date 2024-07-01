N = int(input())

X_list = []
Y_list = []

for i in range(N):
    X, Y = map(int, input().split())
    X_list.append(X)
    Y_list.append(Y)

print((max(X_list)-min(X_list))*(max(Y_list)-min(Y_list)))