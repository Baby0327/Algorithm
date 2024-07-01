import sys

n, m = map(int, sys.stdin.readline().split())

test = {}
group = []
for i in range(n):
    name = sys.stdin.readline().rstrip()
    group.append(name)
    members = int(sys.stdin.readline())
    for j in range(members):
        if j == 0:
            test[name] = [sys.stdin.readline().rstrip()]
        else:
            test[name].append(sys.stdin.readline().rstrip())

for i in range(m):
    word = sys.stdin.readline().rstrip()
    num = int(sys.stdin.readline())
    if num == 1:
        for j in group:
            if word in test[j]:
                sys.stdout.write(str(j) + '\n')
    else:
        result = sorted(test[word])
        for j in result:
            sys.stdout.write(str(j)+'\n')