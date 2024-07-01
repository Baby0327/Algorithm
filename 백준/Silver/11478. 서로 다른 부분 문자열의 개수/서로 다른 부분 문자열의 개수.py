S = input()

num = 1
result = set()
for i in range(len(S)):
    x = 0
    for j in range(len(S)-num+1):
        result.add(S[x:x+num])
        x += 1
    num += 1

print(len(result))