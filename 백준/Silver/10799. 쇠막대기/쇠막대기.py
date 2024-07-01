bracket = list(input())
test = [0]
result = 0
i = 0
while i < len(bracket):
    if bracket[i] == '(' and bracket[i+1] == ')':
        result += (len(test)-1)
        i += 2
    elif bracket[i] == ')' and bracket[i-1] == ')':
        test.pop()
        result += 1
        i += 1
    else:
        test.append(bracket[i])
        i += 1

print(result)