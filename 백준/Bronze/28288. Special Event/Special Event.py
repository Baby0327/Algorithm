result = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]

for i in range(int(input())):
    s = input()
    for j in range(len(s)):
        if s[j] == "Y":
            result[j][0] += 1

result.sort(key=lambda x : -x[0])

print(",".join(str(i[1]) for i in list(filter(lambda x : x[0] == result[0][0], result))))