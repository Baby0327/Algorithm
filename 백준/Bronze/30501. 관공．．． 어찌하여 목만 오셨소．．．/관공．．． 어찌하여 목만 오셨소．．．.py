n = int(input())
name = [input() for _ in range(n)]

for i in name:
    if "S" in i:
        print(i)
        break