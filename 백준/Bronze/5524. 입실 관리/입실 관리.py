N = int(input())

for i in range(N):
    result = list(input())
    for i in range(len(result)):
        if ord(result[i]) < 97:
            result[i] = chr(ord(result[i])+32)
    print("".join(result))