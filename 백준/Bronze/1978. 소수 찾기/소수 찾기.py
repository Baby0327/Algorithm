n = int(input())
num = list(map(int, input().split()))
result = 0

for i in num:
    test = 0
    if i > 1:
        for j in range(2,i): # 하나라도 나눠 떨어지는 값이 있으면 끝...
            if i % j == 0:
                test += 1
                break
        if test == 0:
            result += 1

print(result)