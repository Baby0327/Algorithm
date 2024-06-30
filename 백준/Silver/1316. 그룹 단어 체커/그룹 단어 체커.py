N = int(input())
result = []

for i in range(N):
    line = list(input())
    tmp = 0
    for x in range(len(line)): # 각각의 케이스 분석
        for y in range(0,x+1): # 각 케이스 기준 앞의 원소들과 비교
            if line[x] == line[y]: # 앞의 원소와 같은 원소가 등장하면.
                if x - y > 1:   # 심지어 두 원소의 인덱스가 연속적이지 않다면
                    for j in range(y, x+1):
                        if line[j] != line[y]:
                            tmp = 1
                            break
    if tmp == 1:
        result.append("NO")
    else:
        result.append("YES")

print(result.count('YES'))