N, K = map(int, input().split())

top = 1
bottom = 1
for i in range(N, N-K, -1):
    top *= i
for i in range(1,K+1):
    bottom *= i

print(top//bottom)