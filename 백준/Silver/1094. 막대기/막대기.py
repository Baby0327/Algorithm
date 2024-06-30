X = int(input())

test = 64
result = 0
while X != 0:
    if test <= X:
        result += 1
        X -= test
    test //= 2

print(result)