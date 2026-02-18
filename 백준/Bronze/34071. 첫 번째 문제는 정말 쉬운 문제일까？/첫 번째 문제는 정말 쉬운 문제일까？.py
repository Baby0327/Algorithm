x = [int(input()) for _ in range(int(input()))]
first = x[0]
x.sort()

if first == x[0]:
    print("ez")
elif first == x[-1]:
    print("hard")
else:
    print("?")