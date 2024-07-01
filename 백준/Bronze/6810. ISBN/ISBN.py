num = "9780921418"

for i in range(3):
    num += input()

result = 0
for i in range(13):
    if i % 2 == 1:
        result += 3 * int(num[i])
    else:
        result += int(num[i])

print(f"The 1-3-sum is {result}")