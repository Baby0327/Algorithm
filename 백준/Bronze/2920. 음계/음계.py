num = list(map(int, input().split()))
num_1 = sorted(num)
num_2 = sorted(num, reverse=True)

if num == num_1:
    print("ascending")
elif num == num_2:
    print("descending")
else:
    print("mixed")