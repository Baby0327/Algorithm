num_list = []
result = []

while True:
    num = str(input())
    if num == "0":
        break
    num_list.append(num)

for i in num_list:
    line = list(i)
    L = len(line)
    j = 0
    while True:
        if line[j] == line[L-j-1]:
            j += 1
            if j == L//2 + 1:
                case = "yes"
                result.append(case)
                break
        else:
            case = "no"
            result.append(case)
            break

for i in result:
    print(i)