N = int(input())

result = []
for i in range(N):
    result.append(input())

for i in range(N):
    print(str(i+1)+". "+result[i])