N = int(input())
result = []

for i in range(N):
    A, B = map(int, input().split())
    result.append(A+B)

for i in range(N):
    print(result[i])