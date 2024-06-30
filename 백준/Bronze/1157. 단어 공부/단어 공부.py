ABC = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
result = [0 for i in range(26)]

word = list(input())

for i in word:
    for j in ABC:
        for k in j:
            if i == k:
                result[ABC.index(j)] += 1

tmp = max(result)

count = 0
for i in result:
    if i == tmp:
        count += 1

if count >= 2:
    print("?")
else:
    for i in ABC[result.index(max(result))]:
        print(i)
        break