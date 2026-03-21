k, l = map(int, input().split())
check = 1
n = 0

for i in range(2, l):
    if k % i == 0:
        check = 0
        n = i
        break

print("GOOD" if check else f"BAD {i}")