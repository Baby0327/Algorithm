a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

count = 0
for i in range(n0,n0+100):
    if a1*i+a0 <= c*i:
        count += 1

if count == 100:
    print(1)
else:
    print(0)