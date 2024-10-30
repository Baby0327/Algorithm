dic = {}

for i in range(int(input())):
    s = input()
    for j in range(len(s)):
        dic.setdefault(s[j], []).append(len(s) - j - 1)

num = sorted(dic.values(), key=lambda x : sum(10**i for i in x), reverse=True)
total = 0

for i in range(len(num)):
    for j in num[i]:
        total += (9 - i) * 10**j

print(total)