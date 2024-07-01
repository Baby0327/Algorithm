def makingTree(depth, arr):

    mid = len(arr)//2
    tree[depth].append(arr[mid])

    if len(arr) != 1:
        makingTree(depth + 1, arr[:mid])
        makingTree(depth + 1, arr[mid + 1:])


k = int(input())
num = list(map(int, input().split()))
tree = [[] for i in range(k)]

makingTree(0, num)

for i in range(k):
    for j in tree[i]:
        print(j, end=" ")
    print()