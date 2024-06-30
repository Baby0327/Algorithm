import sys

N = int(sys.stdin.readline())
test = []
for i in range(N):
    test.append(sys.stdin.readline().rstrip())

test.sort(key=lambda x: len(x))

result = []
for i in range(N):
    for j in range(i+1, N, +1):
        if test[j][:len(test[i])] == test[i]:
            result.append(test[i])
            break

print(N-len(result))