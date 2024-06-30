A, B = map(int, input().split())
N = int(input())
save = []
for i in range(N):
    save.append(int(input()))

if A >= B:
    original = A-B
else:
    original = B-A

for i in range(len(save)):
    if save[i]-B >= 0:
        save[i] = save[i]-B
    else:
        save[i] = B-save[i]

save.sort()

print(min(save[0]+1, original))