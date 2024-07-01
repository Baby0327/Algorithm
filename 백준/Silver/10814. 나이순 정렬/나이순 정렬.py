N = int(input())

user = []
for i in range(N):
    user.append(input().split())

user.sort(key=lambda x: int(x[0]))

for i in user:
    print(i[0], i[1])