import sys

count = 1
while True:
    S = list(sys.stdin.readline().rstrip())

    if '-' in S:
        break

    test = []
    for i in range(len(S)):
        if len(test) == 0:
            test.append(S[i])
        else:
            if S[i] == '}' and test[-1] == '{':
                test.pop()
            else:
                test.append(S[i])

    result = 0
    for i in range(len(test)):
        if i % 2 == 0:
            if test[i] == '}':
                result += 1
        else:
            if test[i] == '{':
                result += 1

    print(f"{count}. {result}")
    
    count += 1