N = int(input())

result = []
for i in range(N):
    tmp = list(input().split(" "))
    tmp.reverse()
    result.append(" ".join(tmp))

for i in range(N):
    print("Case #{}:".format(i+1), result[i])