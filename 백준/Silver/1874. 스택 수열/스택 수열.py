import sys

n = int(sys.stdin.readline())
test = []
for i in range(n):
    test.append(int(sys.stdin.readline()))

tmp = []
output = []
i = 0
j = 1
X = True
while i < n or j <= n:
    if test[i] >= j:
        tmp.append(j)
        output.append("+")
        j += 1
    elif test[i] == tmp[-1]:
        tmp.pop()
        output.append("-")
        i += 1
    else:
        X = False
        break


if X:
    for i in output:
        print(i)
else:
    print("NO")