D, H, W = map(int, input().split())

X = pow(D**2/(H**2+W**2),1/2)

print(int(X*H), int(X*W))