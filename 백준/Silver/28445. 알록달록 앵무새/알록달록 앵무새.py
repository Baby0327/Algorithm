c = sorted(list(set(input().split() + input().split())))

for i in c:
    for j in c:
        print(i, j)