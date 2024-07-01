test = [0] * 7
test[0] = "Never gonna give you up"
test[1] = "Never gonna let you down"
test[2] = "Never gonna run around and desert you"
test[3] = "Never gonna make you cry"
test[4] = "Never gonna say goodbye"
test[5] = "Never gonna tell a lie and hurt you"
test[6] = "Never gonna stop"

n = int(input())

result = "No"
for i in range(n):
    word = input()
    if word not in test:
        result = "Yes"
        break

print(result)