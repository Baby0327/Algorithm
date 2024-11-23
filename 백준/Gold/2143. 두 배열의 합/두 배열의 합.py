import sys
input = sys.stdin.readline

def total_calc(list, l):
    temp = [0]

    for i in range(l):
        temp.append(temp[-1] + list[i])

    return temp

def dict_calc(total, l):
    dict = {}

    for i in range(l + 1):
        for j in range(i):
            temp = total[i] - total[j]

            if dict.get(temp, 0):
                dict[temp] += 1
            else:
                dict[temp] = 1

    return dict

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
total_a = total_calc(a, n)
total_b = total_calc(b, m)
dict_a = dict_calc(total_a, n)
dict_b = dict_calc(total_b, m)
result = 0

for i in dict_a.keys():
    temp = t - i

    if dict_b.get(temp, 0):
        result += dict_a[i] * dict_b[temp]

print(result)