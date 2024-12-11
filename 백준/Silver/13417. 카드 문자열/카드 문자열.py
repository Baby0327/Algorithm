import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    char = input().rstrip().split()
    result = ""

    while char:
        if result and result[0] >= char[0]:
            result = char[0] + result
        else:
            result += char[0]

        char = char[1:]

    print(result)