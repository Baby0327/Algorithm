"""
호텔 방 번호
"""

while True:
    try:
        n, m = map(int, input().split())
        result = 0

        for i in range(n, m+1):
            if len(str(i)) == len(set(list(str(i)))):
                result += 1

        print(result)

    except EOFError:
        break