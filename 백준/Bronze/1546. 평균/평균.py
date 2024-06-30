N = int(input())
score = list(map(int, input().split()))

best = 0
for i in score:
    if i > best:
        best = i

result = []

change = 0
for i in score:
    change += i/best*100

print(change/N)