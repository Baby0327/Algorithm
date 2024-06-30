import sys

result = []
test = ['a','e','i','o','u','A','E','I','O','U']

while True:
    tmp =list(sys.stdin.readline().rstrip())
    if tmp == ['#']:
        break
    count = 0
    for i in tmp:
        if i in test:
            count += 1
    result.append(count)

for i in result:
    print(i)