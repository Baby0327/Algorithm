S = list(input())
result = [0 for i in range(26)]

for i in S:
    result[ord(i)%97] += 1

for i in result:
    print(i, end=" ")