N = int(input())
size = list(map(int, input().split()))
size.sort(reverse=True)


score = 0
while len(size)!=1:
    score += size[0]*size[1]
    tmp = size[0]+size[1]
    size.remove(size[0])
    size[0] = tmp

print(score)