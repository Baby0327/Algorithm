N = int(input())

result = None
for i in range(N+1):
    tmp = i
    length = list(map(int, str(tmp)))
    if len(length) == 1:
        if i + sum(length) == N:
            result = i
            print(result)
            break
    else:
        if i + sum(length) == N:
            result = i
            print(result)
            break

if result == None:
    print(0)