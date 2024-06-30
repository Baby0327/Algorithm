M, N = map(int, input().split())
num = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
       6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}

eng = []
for i in range(M, N+1):
    tmp = list(map(int, str(i)))
    for j in range(len(tmp)):
        tmp[j] = num[tmp[j]]
    eng.append(" ".join(tmp))

eng.sort()
num = {v:k for k,v in num.items()}

result = []
for i in eng:
    tmp = list(i.split())
    for i in range(len(tmp)):
        tmp[i] = str(num[tmp[i]])
    result.append(int("".join(tmp)))


for i in range(len(result)):
    if i != 0 and i % 10 == 0:
        print()
    print(result[i], end=" ")