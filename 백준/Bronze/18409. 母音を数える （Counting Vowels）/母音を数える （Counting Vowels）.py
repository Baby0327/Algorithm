n = int(input())
s = input()
test = ['a', 'i', 'u', 'e', 'o']
result = 0
for i in s:
    if i in test:
        result += 1

print(result)