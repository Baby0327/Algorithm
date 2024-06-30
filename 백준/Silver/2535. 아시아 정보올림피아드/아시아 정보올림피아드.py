def score(x):
    return x[2]


N = int(input())

contest = []
for i in range(N):
    contest.append(list(map(int, input().split())))

contest.sort(key=score, reverse=True)

country = []
for i in range(N):
    country.append(contest[i][0])

country = set(country)

country = [0 for i in range(len(country)+1)]

result = []
i = 0
while len(result) != 3:
    tmp = contest[i]
    country[tmp[0]] += 1
    if country[tmp[0]] > 2:
        i += 1
        continue
    else:
        result.append(tmp)
        i += 1

for i in result:
    print(i[0], i[1])