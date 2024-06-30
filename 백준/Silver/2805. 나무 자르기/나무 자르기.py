import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
tree = list(map(int, sys.stdin.readline().rstrip().split()))
tree.sort()

left = 0
right = max(tree)
tmp = 0
while True:
    center = (left+right)//2
    for i in tree:
        if i >= center:
            tmp = tree[tree.index(i):]
            break
    if sum(tmp) - center*len(tmp) > M:
        left = center
    elif sum(tmp) - center*len(tmp) < M:
        right = center
    else:
        print(center)
        break

    if left +1 == right:
        print(left)
        break