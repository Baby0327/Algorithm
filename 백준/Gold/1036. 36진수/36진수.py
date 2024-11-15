import sys
input = lambda : sys.stdin.readline().rstrip()

def change(n):
    answer = ""

    while n > 0:
        n, mod = divmod(n, 36)

        if mod <= 9:
            answer += str(mod)
        else:
            answer += chr(mod + 55)

    return answer[::-1] or 0

dict = {}
result = []
n = int(input())

for _ in range(n):
    num = input()
    result.append(num)

    for i in range(len(num)):
        if num[i].isdigit():
            now = int(num[i])
        else:
            now = ord(num[i]) - 55

        dict[num[i]] = dict.get(num[i], 0) + (36**(len(num) - i - 1) * (35 - now))

count = sorted(dict.items(), key=lambda x : (-x[1]))

for i in range(min(len(count), int(input()))):
    for j in range(n):
        result[j] = result[j].replace(count[i][0], "Z")

print(change(sum(int(i, 36) for i in result)))