s = input()
c = set(s)
result = []

for i in c:
    result.append(s.count(i) % 2)

if sum(result) == 0:
    print(0)
elif sum(result) == len(c):
    print(1)
else:
    print(2)