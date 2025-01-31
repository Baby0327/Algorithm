n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))

for i in range(n):
    print("yes" if p.count(i + 1) > c[i] else "no")