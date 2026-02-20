n = int(input())
p = int(input())
result = []

if n >= 5:
    result.append(p-500)
    if n >= 10:
        result.append(int(p*0.9))
        if n >= 15:
            result.append(p-2000)
            if n >= 20:
                result.append(int(p*0.75))
else:
    result.append(p)

print(max(min(result), 0))