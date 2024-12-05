n = int(input())
s = [list(input()) for _ in range(n)]
check = 1

for i in range(n):
    for j in range(n):
        if s[i][j] != s[j][i]:
            check = 0
            break

print("YES" if check else "NO")