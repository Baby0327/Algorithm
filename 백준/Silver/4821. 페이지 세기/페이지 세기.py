"""
페이지 세기
"""

while True:
    t = int(input())

    if not t:
        break

    page = input().split(",")
    result = [0] * (t+1)

    for i in page:
        count = i.split("-")

        if (len(count) == 2) and (int(count[0]) <= int(count[1])) and (int(count[0]) <= t):
            if (int(count[1]) <= t):
                for j in range(int(count[0]), int(count[1]) + 1):
                    result[j] = 1
            else:
                for j in range(int(count[0]), t + 1):
                    result[j] = 1
        elif len(count) == 1 and int(count[0]) <= t:
            result[int(count[0])] = 1

    print(result.count(1))