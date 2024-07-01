N = int(input())

for i in range(N):
    tmp = input()
    if 6 <= len(tmp) <= 9:
        print("yes")
    else:
        print("no")